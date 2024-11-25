from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get('http://the-internet.herokuapp.com/inputs')

# Введите в поле текст 1000
number = driver.find_element(By.CSS_SELECTOR, 'input')
sleep(1)
number.send_keys('1000')
sleep(1)

# Очистите это поле (метод clear).
number.clear()
sleep(1)

# Введите в это же поле текст 999
number.send_keys('999')
sleep(1)
driver.quit()


