from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://testautomationpractice.blogspot.com/')

a = driver.find_element('class name', 'wikipedia-icon')
b = driver.find_element('id', 'Wikipedia1_wikipedia-search-input')
c = driver.find_element('class name', 'wikipedia-search-button')
d = driver.find_element('tag name', 'input')

time.sleep(3)
driver.quit()