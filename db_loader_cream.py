from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

is_on_page = True
no_page = 1

while is_on_page:
    try:
        driver.get(f"https://www.saq.com/fr/produits?p={no_page}")

        names = driver.find_elements(By.CLASS_NAME, "product-item-link")
        names_list = []
        for p in range(len(names)):
            names_list.append(names[p].text)

        descriptions = driver.find_elements(
            By.CLASS_NAME, "product-item-identity-format"
        )
        categories_list = []
        size_list = []
        for p in range(len(descriptions)):
            text = descriptions[p].text.split(" | ")
            categories_list.append(text[0].strip())
            size_list.append(text[1].strip())

        prices = driver.find_elements(By.CLASS_NAME, "price")
        prices_list = []
        for p in range(len(prices)):
            prices_list.append(prices[p].text)

        if no_page < 500:
            no_page += 1
        else:
            is_on_page = False
    except:
        is_on_page = False
