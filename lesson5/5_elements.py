from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://qa.price-port.ru/')

a = driver.find_element(By.ID, "contact-form-anchor") # Поиск по id атрибуту
print(a)
assert a == driver.find_element('id', "contact-form-anchor")

c = driver.find_element(By.TAG_NAME, "input") # Поиск по имени тега
print(c)

b = driver.find_element(By.CLASS_NAME, "button.button_accent.button-icon.header__button-personal") # Поиск по имени класса
print(b)
b.click()

time.sleep(3)
driver.quit()

"""
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
"""