import allure
from selenium.webdriver.common.by import By


class TotalPage:

    def __init__(self, driver):
        self._driver = driver

    def cart_total(self):
        with allure.step("Получить итоговую сумму товаров"):
            return self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
