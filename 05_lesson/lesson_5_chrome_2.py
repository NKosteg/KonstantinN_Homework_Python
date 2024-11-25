from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get('http://uitestingplayground.com/dynamicid')

# Кликните на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
sleep(2)
driver.quit()
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.