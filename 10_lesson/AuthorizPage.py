import allure
from selenium.webdriver.common.by import By


class AuthorizationPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    @allure.step("Авторизоваться пользователем с логином: {user_name} и паролем: {password}")
    def authorization(self, user_name: str, password: str) -> None:
        with allure.step("Найти поле 'Username' по селектору"):
            user = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Очистить поле 'Username'"):
            user.clear()
        with allure.step("Ввести в поле 'Username' данные"):
            user.send_keys(user_name)
        with allure.step("Найти поле 'Password' по селектору"):
            passw = self._driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Очистить поле 'Password'"):
            passw.clear()
        with allure.step("вести в поле 'Password' данные"):
            passw.send_keys(password)
        with allure.step("Нажать 'Login'"):
            self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
