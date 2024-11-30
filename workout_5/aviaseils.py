import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.aviasales.ru/")

where_from = driver.find_element(By.CSS_SELECTOR, "#avia_form_origin-input")
where_from.send_keys(Keys.BACKSPACE)
time.sleep(2)
where_from.send_keys("Нью-Йорк")

time.sleep(2)
where = driver.find_element(By.CSS_SELECTOR, "#avia_form_destination-input")
where.send_keys("Chicago")
time.sleep(2)

when = driver.find_element(By.CSS_SELECTOR, "[data-test-id='departure-calendar-icon']")
when.click()
when.click()
time.sleep(2)

data1 = driver.find_element(By.CSS_SELECTOR, '[data-test-id="date-29.11.2024"]')
data1.click()

back = driver.find_element(By.CSS_SELECTOR, "[data-test-id='end-date-field']")
back.click()
time.sleep(2)

data2 = driver.find_element(By.CSS_SELECTOR, "[data-test-id='date-05.12.2024']")
data2.click()
time.sleep(2)

button_find = driver.find_element(By.CSS_SELECTOR, "[data-test-id='form-submit']")
button_find.click()

sleep(10)







