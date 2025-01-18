import allure
from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Добавить товары в корзину")
    def add_products(self) -> None:
        with allure.step("Добавить в корзину Sauce Labs Backpack"):
            self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        with allure.step("Добавить в корзину Sauce Labs Bolt T-Shirt"):
            self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        with allure.step("Добавить в корзину Sauce Labs Onesie"):
            self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        with allure.step("Перейти в корзину"):
            self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
        with allure.step("Перейти на страницу оформления"):
            self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
