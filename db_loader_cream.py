from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
import csv

from infrastructure.database.user_database import UserDatabase
from domain.models.customer import Customer
from domain.factories.user_factory import UserFactory


def scrap_products_infos():
    """Scrap products infos from SAQ website and save them in a csv file"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    names_list = []
    categories_list = []
    size_list = []
    prices_list = []
    image_list = []
    for no_page in range(10):
        try:
            driver.get(f"https://www.saq.com/fr/produits?p={no_page}")

            names_list = [
                name.text
                for name in driver.find_elements(By.CLASS_NAME, "product-item-link")
            ]

            description_list = [
                desc.text.split(" | ")
                for desc in driver.find_elements(
                    By.CLASS_NAME, "product-item-identity-format"
                )
            ]

            size_list = [desc[1].strip() for desc in description_list]

            image_list = [
                image.get_attribute("src")
                for image in driver.find_elements(By.CLASS_NAME, "product-image-photo")
            ]

            prices_list = [
                price.text.replace('"', "")
                for price in driver.find_elements(By.CLASS_NAME, "price")
            ]

            categories_list = [desc[0].strip() for desc in description_list]

        except:
            print(f"Page {no_page} not found")

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

    # push here in DB


def store_customers_infos():
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

            phone_number = phone_number.replace("(", "")
            phone_number = phone_number.replace(")", "")
            phone_number = phone_number.replace("-", "")
            phone_number = phone_number.replace(" ", "")

            while len(phone_number) < 10:
                phone_number = "0" + phone_number

            while len(phone_number) > 10:
                phone_number = phone_number[1:]

            phone_number = (
                phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]
            )

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


def store_sellers_infos():
    # Data generated with https://generatedata.com/generator, saved as csv file sellers.csv
    usernames_list = []
    passwords_list = []
    names_list = []
    descriptions_list = []
    addresses_list = []
    phone_numbers_list = []
    emails_list = []

    # push here in DB


store_customers_infos()
