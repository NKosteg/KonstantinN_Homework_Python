from selenium.webdriver.common.by import By


class AuthorizationPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    def authorization(self, user_name, password):
        user = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        user.clear()
        user.send_keys(user_name)
        passw = self._driver.find_element(By.CSS_SELECTOR, '#password')
        passw.clear()
        passw.send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
