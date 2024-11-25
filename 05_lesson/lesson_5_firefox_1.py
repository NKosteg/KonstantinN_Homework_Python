from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(2)
# В модальном окне нажмите на кнопку Сlose
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/p').click()
sleep(2)
driver.quit()