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

driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
driver.get(ROOM_WEBSITE)
driver.maximize_window()

scroll_down = driver.find_element_by_xpath('//*[@id="search-page-list-container"]')
for i in range(4):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
    time.sleep(2)

for i in range(5):
    price = driver.find_elements_by_class_name("list-card-price")
 
    for i in price:
        print(i.text)



time.sleep(600)