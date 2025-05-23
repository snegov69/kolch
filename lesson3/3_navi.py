from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://qa.price-port.ru/')
PAGE_TITLE = driver.title # Записываем значение title в переменную page_title
assert driver.title == "ПрайсПорт", "Страница не открылась"
print("Title страницы: ", PAGE_TITLE) # Выводим значение переменной на экран
time.sleep(2)
driver.refresh

driver.get('https://qa.price-port.ru/agreement.pdf')
time.sleep(2)
PAGE_URL = driver.current_url # Получаем текущий URL-адрес в переменную
print(PAGE_URL) # Выводим значение переменной

time.sleep(3)
driver.quit()