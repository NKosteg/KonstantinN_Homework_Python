from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(4)

    def input_value(self, selector, data):
        text_input_field = self._driver.find_element(By.NAME, selector)
        text_input_field.clear()
        text_input_field.send_keys(data)

    def button_click(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button').click()

    def checking_input(self, id_element):
        return self._driver.find_element(By.CSS_SELECTOR, id_element).value_of_css_property('color')

    def checking_empty_input(self, id_element):
        return self._driver.find_element(By.CSS_SELECTOR, id_element).value_of_css_property('color')
