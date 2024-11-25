from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get('http://the-internet.herokuapp.com/login')

# В поле username введите значение tomsmith
username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys('tomsmith')
sleep(1)

# В поле password введите значение SuperSecretPassword!
password =driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('SuperSecretPassword!')
sleep(1)

# Нажмите кнопку Login
driver.find_element(By.CSS_SELECTOR, 'button').click()
sleep(2)
driver.quit()