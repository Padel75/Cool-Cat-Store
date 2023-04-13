import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

from domain.factories.product_factory import ProductFactory
from domain.models.product import Product
from domain.models.seller import Seller
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
    def loadDb(self):
        self.__store_sellers_infos()
        self.__store_customers_infos()
        self.__store_products_infos()

    def __scrap_products_infos(self):
        """Scrap products infos from SAQ website and save them in a csv file"""
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        names_list = []
        description_list = []
        categories_list = []
        size_list = []
        prices_list = []
        image_list = []

        for no_page in range(10):
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
                row = [
                    names_list[no_page],
                    size_list[no_page],
                    image_list[no_page],
                    prices_list[no_page],
                    categories_list[no_page],
                ]
                writer.writerow(row)

    def __store_products_infos(self):
        """Store products infos in DB"""
        # Data generated with https://generatedata.com/generator, saved as csv file products.csv

        self.__scrap_products_infos()

        database: ProductDatabase = ProductDatabase()
        factory: ProductFactory = ProductFactory()

        with open("products.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    name = row[0]
                    size = row[1]
                    image = row[2]
                    price = row[3]
                    category = row[4]

                    product_infos = {
                        "name": name,
                        "size": size,
                        "image_src": image,
                        "price": price,
                        "category": category,
                        "seller_id": randint(1, 200),
                    }

                    product: Product = factory.create_product(product_infos)

                    database.create_product(product)

    def __store_customers_infos(self):
        """Store customers infos in DB"""
        # Data generated with https://generatedata.com/generator, saved as csv file customers.csv

        database: UserDatabase = UserDatabase()
        factory: UserFactory = UserFactory()

        with open("customers.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                password = row[0]
                name = row[1]
                last_name = row[2]
                address = row[3]
                phone_number = row[4]
                email = row[5]

                username = name.lower() + last_name.lower()

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

    def __store_sellers_infos(self):
        """Store sellers infos in DB"""
        # Data generated with https://generatedata.com/generator, saved as csv file sellers.csv

        database: UserDatabase = UserDatabase()
        factory: UserFactory = UserFactory()

        with open("sellers.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                # password,name,description,address,phone,email
                password = row[0]
                name = row[1]
                description = row[2]
                address = row[3]
                phone_number = row[4]
                email = row[5]

                username = name.lower().replace(" ", "")

                phone_number: str = format_phone_number(phone_number)

                seller_infos = {
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

    def __store_paiement_system(self):
        pass

    def __store_sellers_products(self):
        pass

    def __customer_buy_product(self):
        # TODO: add a product to the cart
        # TODO: pay for the product
        pass


loader = DbLoader()
loader.loadDb()
