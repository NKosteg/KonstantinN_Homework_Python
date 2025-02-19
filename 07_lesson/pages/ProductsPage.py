from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self._driver = driver

    def add_products(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
