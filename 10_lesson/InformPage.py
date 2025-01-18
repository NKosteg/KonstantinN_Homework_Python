import allure
from selenium.webdriver.common.by import By


class InformationPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Заполнить поле формы")
    def your_information(self):
        with allure.step("Найти поле 'First Name' по селектору"):
            first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        with allure.step("Очистить поле 'First Name'"):
            first_name.clear()
        with allure.step("Ввести в поле 'First Name' данные 'Константин'"):
            first_name.send_keys('Константин')
        with allure.step("Найти поле 'Last Name' по селектору"):
            last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        with allure.step("Очистить поле 'Last Name'"):
            last_name.clear()
        with allure.step("Ввести в поле 'Last Name' данные 'Николаев'"):
            last_name.send_keys('Николаев')
        with allure.step("Найти поле 'Zip/Postal Code' по селектору"):
            postal_code = self._driver.find_element(By.CSS_SELECTOR, '#postal-code')
        with allure.step("Очистить поле 'Zip/Postal Code'"):
            postal_code.clear()
        with allure.step("Ввести в поле 'Zip/Postal Code' данные '191014'"):
            postal_code.send_keys('191014')
        with allure.step("Нажать 'Continue'"):
            self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
