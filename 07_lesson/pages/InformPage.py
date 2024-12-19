from selenium.webdriver.common.by import By


class InformationPage:

    def __init__(self, driver):
        self._driver = driver

    def your_information(self):
        first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.clear()
        first_name.send_keys('Константин')
        last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.clear()
        last_name.send_keys('Николаев')
        postal_code = self._driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.clear()
        postal_code.send_keys('191014')
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
