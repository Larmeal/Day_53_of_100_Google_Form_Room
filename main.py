from selenium.webdriver.common.keys import Keys
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import time

dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

GOOGLE_FORM = os.getenv("GOOGLE_FORM")
ROOM_WEBSITE = os.getenv("ROOM_WEBSITE")
CHROME_DRIVER = "C:\Developer\chromedriver.exe"

header = {
    "Accept-Language": "en-US,en;q=0.9,th;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

response = requests.get(ROOM_WEBSITE, headers=header)
content = response.text

soup = BeautifulSoup(content, "html.parser")
price = soup.find_all(name="div", class_="list-card-price")
price_per_mouth = [mouth.getText().split("/")[0].split("+")[0] for mouth in price]

address = soup.find_all(name="address", class_="list-card-addr" )
address_str = [add.getText().replace(" |", ",") for add in address]

add_website = "https://www.zillow.com"
link = soup.find_all(name="a", class_="list-card-link")
link_str = [link_.get("href").replace(add_website, "") for link_ in link][:9]
full_link = [f"{add_website}{full}" for full in link_str]

driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
driver.get(GOOGLE_FORM)
driver.maximize_window()

for i in range(len(address)):
    time.sleep(5)

    add_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_address.send_keys(address_str[i])

    add_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_price.send_keys(price_per_mouth[i])

    add_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_link.send_keys(full_link[i])
    
    send_data = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_data.click()

    time.sleep(2)

    send_again = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_again.click()

time.sleep(600)
