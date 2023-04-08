from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
import csv


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

            names_list = [name.text for name in driver.find_elements(By.CLASS_NAME, "product-item-link")]

            description_list = [desc.text.split(" | ") for desc in
                                driver.find_elements(By.CLASS_NAME, "product-item-identity-format")]

            size_list = [desc[1].strip() for desc in description_list]

            image_list = [image.get_attribute("src") for image in
                          driver.find_elements(By.CLASS_NAME, "product-image-photo")]

            prices_list = [price.text.replace('"', "") for price in driver.find_elements(By.CLASS_NAME, "price")]

            categories_list = [desc[0].strip() for desc in description_list]



        except:
            print(f"Page {no_page} not found")

    with open("products.csv", "w") as f:
        writer = csv.writer(f)

        for no_page in range(len(names_list)):
            row = [names_list[no_page], size_list[no_page], image_list[no_page], prices_list[no_page], categories_list[no_page]]
            writer.writerow(row)

    # push here in DB

def scrap_customers_infos():
    # Data generated with https://generatedata.com/generator, saved as csv file customers.csv
    usernames_list = []
    passwords_list = []
    first_names_list = []
    last_names_list = []
    addresses_list = []
    phone_numbers_list = []
    emails_list = []

    # push here in DB
