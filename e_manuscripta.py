""" This script uses selenium to open the e-manuscripta website, search for a term and download the images."""
import os
import shutil
import time

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SEARCH_TERM = "rise"

# Define a download directory and create it if necessary
image_path = os.path.join(os.getcwd(), "images")
if not os.path.exists(image_path):
    os.makedirs(image_path)

# start by defining the options
options = webdriver.ChromeOptions()

# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'

# This returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

# Pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.maximize_window()
driver.implicitly_wait(5)


# Open the archive page
url = f"https://www.e-manuscripta.ch/"
driver.get(url)
time.sleep(4)

# Find the search field, enter the search term and press enter
search_field = driver.find_element(By.ID, "mobileQuicksearch")
search_field.send_keys(SEARCH_TERM)
search_field.send_keys(Keys.ENTER)
time.sleep(3)

search_list = driver.find_element(By.ID, "searchResult")
search_results = search_list.find_elements(By.TAG_NAME, "li")
for result in search_results:
    try:
        result_image = result.find_element(By.TAG_NAME, "img")
        img_src = result_image.get_attribute("src")

        response = requests.get(img_src, stream=True)
        with open(os.path.join(image_path, img_src.split('/')[-1]+'.jpg'), 'wb') as f_out:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f_out)
            print("image saved")

    except NoSuchElementException:
        print("no image found")

print("Done!")
