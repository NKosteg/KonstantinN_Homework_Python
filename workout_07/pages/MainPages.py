from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

class MainPage:


    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get('https://www.labirint.ru/')

    def set_cookie_policy(self):
        my_cookie = {
            'name': 'cookie_policy',
            'value': '1'
        }
        self._driver.add_cookie(my_cookie)

    def search(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

