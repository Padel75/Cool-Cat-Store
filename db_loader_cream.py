import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint, choice

from domain.factories.product_factory import ProductFactory
from domain.models.product import Product
from domain.models.seller import Seller
from infrastructure.database.database import Database
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from domain.models.customer import Customer
from domain.factories.user_factory import UserFactory


def format_phone_number(phone_number: str) -> str:
    formatted_phone_number = phone_number.replace("(", "")
    formatted_phone_number = formatted_phone_number.replace(")", "")
    formatted_phone_number = formatted_phone_number.replace("-", "")
    formatted_phone_number = formatted_phone_number.replace(" ", "")

    while len(formatted_phone_number) < 10:
        formatted_phone_number = "0" + formatted_phone_number

    while len(formatted_phone_number) > 10:
        formatted_phone_number = formatted_phone_number[1:]

    formatted_phone_number = (
        formatted_phone_number[:3]
        + "-"
        + formatted_phone_number[3:6]
        + "-"
        + formatted_phone_number[6:]
    )
    return formatted_phone_number


class DbLoader:
    def loadDb(self) -> None:
        self.__store_sellers_infos()
        self.__store_customers_infos()
        self.__store_products_infos()
        self.__store_payment_systems()

    def __scrap_products_infos(self) -> None:
        """Scrap products infos from SAQ website and save them in a csv file"""
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        names_list: list = []
        description_list: list = []
        categories_list: list = []
        size_list: list = []
        prices_list: list = []
        image_list: list = []

        for no_page in range(100):
            try:
                driver.get(f"https://www.saq.com/fr/produits?p={no_page}")

                names_list.extend(
                    [
                        name.text
                        for name in driver.find_elements(
                            By.CLASS_NAME, "product-item-link"
                        )
                    ]
                )

                description_list.extend(
                    [
                        desc.text.split(" | ")
                        for desc in driver.find_elements(
                            By.CLASS_NAME, "product-item-identity-format"
                        )
                    ]
                )

                size_list.extend([desc[1].strip() for desc in description_list])

                image_list.extend(
                    [
                        image.get_attribute("src")
                        for image in driver.find_elements(
                            By.CLASS_NAME, "product-image-photo"
                        )
                    ]
                )

                prices_list.extend(
                    [
                        price.text.replace('"', "")
                        .replace(" ", "")
                        .replace("$", "")
                        .replace(",", ".")
                        for price in driver.find_elements(By.CLASS_NAME, "price")
                    ]
                )

                categories_list.extend([desc[0].strip() for desc in description_list])

            except:
                print(f"Page {no_page} not found")

        if os.path.exists("products.csv"):
            os.remove("products.csv")

        with open("products.csv", "w") as f:
            writer = csv.writer(f)

            for no_page in range(len(names_list)):
                row: list = [
                    names_list[no_page],
                    size_list[no_page],
                    image_list[no_page],
                    prices_list[no_page],
                    categories_list[no_page],
                ]
                writer.writerow(row)

    def __store_products_infos(self) -> None:
        """Store products infos in DB,
        Data generated with https://generatedata.com/generator, saved as csv file products.csv
        """

        #self.__scrap_products_infos()

        productDatabase: ProductDatabase = ProductDatabase()
        database: Database = Database()
        factory: ProductFactory = ProductFactory()

        with open("products.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    name: str = row[0]
                    size: str = row[1]
                    image: str = row[2]
                    price: str = row[3]
                    category: str = row[4]

                    product_infos = {
                        "name": name,
                        "size": size,
                        "image_src": image,
                        "price": price,
                        "category": category,
                        "seller_id": randint(
                            1,
                            database.select_one_query(
                                "SELECT COUNT(*) FROM sellers", ()
                            )[0],
                        ),
                    }

                    product: Product = factory.create_product(product_infos)

                    productDatabase.create_product(product)

    def __store_customers_infos(self) -> None:
        """Store customers infos in DB,
        Data generated with https://generatedata.com/generator, saved as csv file customers.csv
        """

        database: UserDatabase = UserDatabase()
        factory: UserFactory = UserFactory()

        with open("customers.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                password: str = row[0]
                name: str = row[1]
                last_name: str = row[2]
                address: str = row[3]
                phone_number: str = row[4]
                email: str = row[5]

                username: str = name.lower() + last_name.lower()

                phone_number: str = format_phone_number(phone_number)

                customer_infos = {
                    "first_name": name,
                    "last_name": last_name,
                    "username": username,
                    "password": password,
                    "address": address,
                    "phone_number": phone_number,
                    "email": email,
                }

                customer: Customer = factory.create_customer(customer_infos)

                database.create_customer(customer)

    def __store_sellers_infos(self) -> None:
        """Store sellers infos in DB,
        Data generated with https://generatedata.com/generator, saved as csv file sellers.csv
        """

        database: UserDatabase = UserDatabase()
        factory: UserFactory = UserFactory()

        with open("sellers.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                password: str = row[0]
                name: str = row[1]
                description: str = row[2]
                address: str = row[3]
                phone_number: str = row[4]
                email: str = row[5]

                username: str = name.lower().replace(" ", "")

                phone_number: str = format_phone_number(phone_number)

                seller_infos: dict = {
                    "name": name,
                    "description": description,
                    "username": username,
                    "password": password,
                    "address": address,
                    "phone_number": phone_number,
                    "email": email,
                }

                seller: Seller = factory.create_seller(seller_infos)

                database.create_seller(seller)

    def __store_payment_systems(self) -> None:
        database: Database = Database()

        query: str = "SELECT COUNT(*) FROM customers"
        nb_customers: int = database.select_one_query(query, ())[0]

        query_id_customer: str = "SELECT id FROM customers LIMIT 1"
        first_id_customer: int = database.select_one_query(query_id_customer, ())[0]

        query_payment_systems: str = "INSERT INTO payment_systems (payment_type, number, expiration_date, cvv) VALUES (%s, %s, %s, %s)"
        customer_own_payment_system: str = "INSERT INTO customer_own_payment_system (customer_id, payment_system_id) VALUES (%s, %s)"
        payment_types: list = ["VISA", "MASTERCARD", "AMEX"]

        for no_customer in range(first_id_customer, nb_customers + first_id_customer):
            payment_type: str = choice(payment_types)
            number: str = str(randint(1000000000000000, 9999999999999999))
            expiration_date: str = (
                str(randint(2024, 2030))
                + "-"
                + str(randint(1, 12))
                + "-"
                + str(randint(1, 28))
            )
            cvv: str = str(randint(100, 999))

            values: tuple = (payment_type, number, expiration_date, cvv)

            payment_system_id: int = database.insert_query(
                query_payment_systems, values
            )
            database.insert_query(
                customer_own_payment_system, (no_customer, payment_system_id)
            )
