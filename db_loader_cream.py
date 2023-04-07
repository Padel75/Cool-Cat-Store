from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

is_on_page = True
no_page = 1


names_list = []
categories_list = []
size_list = []
prices_list = []
while is_on_page:
    try:
        driver.get(f"https://www.saq.com/fr/produits?p={no_page}")

        names = driver.find_elements(By.CLASS_NAME, "product-item-link")
        for p in range(len(names)):
            names_list.append(names[p].text)

        descriptions = driver.find_elements(
            By.CLASS_NAME, "product-item-identity-format"
        )
        for p in range(len(descriptions)):
            text = descriptions[p].text.split(" | ")
            categories_list.append(text[0].strip())
            size_list.append(text[1].strip())

        prices = driver.find_elements(By.CLASS_NAME, "price")
        for p in range(len(prices)):
            price = prices[p].text.replace('"', "")
            prices_list.append(price)

        if no_page < 10:
            no_page += 1
        else:
            is_on_page = False
    except:
        is_on_page = False

with open("products.csv", "w") as f:
    writer = csv.writer(f)

    for i in range(len(names_list)):
        row = [names_list[i], categories_list[i], size_list[i], prices_list[i]]
        writer.writerow(row)
