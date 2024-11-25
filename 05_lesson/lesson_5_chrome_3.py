from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get('http://uitestingplayground.com/classattr')

# Кликните на синюю кнопку.
blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
sleep(1)
blue_button.click()
sleep(2)
driver.quit()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
