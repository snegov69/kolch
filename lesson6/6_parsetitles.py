from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://qa.price-port.ru/')

PARSE_TITLES_LIST = driver.find_elements('tag name', "link")
print(*PARSE_TITLES_LIST, sep = '\n')

time.sleep(3)
driver.quit()