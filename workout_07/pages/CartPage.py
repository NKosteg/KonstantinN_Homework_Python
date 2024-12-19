from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self._driver = driver

    def get_cart(self):
        self._driver.get('https://www.labirint.ru/cart/')

    def get_counter(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, '.j-cart-count').text
        return int(txt)
