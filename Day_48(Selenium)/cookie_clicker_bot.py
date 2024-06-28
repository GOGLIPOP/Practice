from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

temp_time = time.time()
start_time = time.time()

while True:
    while True:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()

        if time.time() - temp_time >= 5:
            items = driver.find_elements(By.CSS_SELECTOR, "#store div")

            item_ids = [item.get_attribute("id") for item in items]

            for i in item_ids:
                if i == "":
                    item_ids.pop(int(item_ids.index(i)))

            print(item_ids)
            purchase = driver.find_elements(By.CSS_SELECTOR, "#store div b")
            price_list = [i.text for i in purchase]

            price_list = [price.split(" - ")[-1] for price in price_list if " - " in price]
            all_prices = [int(re.sub(r'[^\d]', '', price)) for price in price_list]

            cookie_upgrades = {all_prices[n]: item_ids[n] for n in range(len(all_prices))}

            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

            max_price = max([price for price in all_prices if price <= money], default=0)

            if max_price > 0:
                buy = driver.find_element(By.ID, cookie_upgrades[max_price])
                buy.click()

            temp_time = time.time()
