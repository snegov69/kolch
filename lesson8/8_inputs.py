from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://testautomationpractice.blogspot.com/')

email_field = driver.find_element('id', 'email')
email_field.clear()
assert email_field.get_attribute('value') == ''
for _ in range(3):
    email_field.send_keys('palevnaya2015@yandex.ru')
    time.sleep(1)
    email_field.clear()
    time.sleep(1)

email_field.send_keys('palevnaya2015@yandex.ru')
email_field_value = email_field.get_attribute("value")
assert 'palevnaya2015@yandex.ru' in email_field_value

time.sleep(3)
driver.quit()