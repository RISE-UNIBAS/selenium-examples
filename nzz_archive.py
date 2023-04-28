""" This script uses selenium to login to the NZZ archive, search for a keyword and a date span and download the
    resulting pdfs."""
import time
import os
from selenium import webdriver
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "your_nzz_username@host.com"
PASSWORD = "your_nzz_password"
SEARCH_TERM = "your_search_term"
EARLIEST_DATE = "01.01.2023"
LATEST_DATE = "31.12.2023"

# start by defining the options
options = webdriver.ChromeOptions()

# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'

# Set the download directory to a local directory and create it if necessary
download_path = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(download_path):
    os.makedirs(download_path)
prefs = {"download.default_directory": download_path}
options.add_experimental_option("prefs", prefs)

# This returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

# Pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.maximize_window()
driver.implicitly_wait(5)

# Open the login page and login
login_url = "https://abo.nzz.ch/registrieren/"
driver.get(login_url)
time.sleep(4)

# Find username field and enter username
user_name_field = driver.find_element(By.ID, "c1-login-field")
user_name_field.send_keys(USERNAME)

# Find login button and click it
login_button = driver.find_element(By.NAME, "checkUserAccount")
login_button.click()
time.sleep(3)

# Find password field and enter password
password_field = driver.find_element(By.ID, "c1-password-field")
password_field.send_keys(PASSWORD)

# Find login button and click it
login_button = driver.find_element(By.ID, "c1-submit-button-login")
login_button.click()
time.sleep(5)

# Open the archive page
url = f"https://zeitungsarchiv.nzz.ch"
driver.get(url)
time.sleep(5)

# Find the search field and enter the search term
search_field = driver.find_element(By.CLASS_NAME, "fup-archive-query-input")
search_field.send_keys(SEARCH_TERM)

# Find the date fields and enter the date range
date_from_field = driver.find_element(By.CLASS_NAME, "fup-s-date-start")
date_from_field.send_keys(EARLIEST_DATE)

date_to_field = driver.find_element(By.CLASS_NAME, "fup-s-date-end")
date_to_field.send_keys(LATEST_DATE)

# Find the search button and click it
my_element = driver.find_element(By.CLASS_NAME, 'fup-button')
my_element.click()
time.sleep(5)

# Find the result list and iterate over it
content = driver.find_elements(By.CLASS_NAME, "fup-archive-result-item")
for item in content:
    # Move the mouse to the item and click it
    a2 = ActionChains(driver)
    a2.move_to_element(item).perform()
    item.click()
    time.sleep(5)

    # Move the mouse to the download button and click it
    a = ActionChains(driver)
    m = driver.find_element(By.CLASS_NAME, "fup-s-submenu-open")
    a.move_to_element(m).perform()
    time.sleep(5)

    download_button = driver.find_element(By.CLASS_NAME, "fup-s-menu-download-page")
    download_button.click()
    time.sleep(5)

    # Find the back button and click it
    back_button = driver.find_element(By.CLASS_NAME, "fup-s-menu-back")
    back_button.click()
    time.sleep(5)

print("Done!")
