from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://qa.price-port.ru/')
time.sleep(2)
driver.refresh
driver.get('https://qa.price-port.ru/agreement.pdf')
time.sleep(5)
PAGE_URL = driver.current_url # Получаем текущий URL-адрес в переменную
print(PAGE_URL) # Выводим значение переменной
driver.quit()