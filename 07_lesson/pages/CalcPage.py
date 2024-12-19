from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def input_delay(self, time):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        input_delay.clear()
        input_delay.send_keys(time)

    def press_buttons(self):
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def output_result(self):
        WebDriverWait(self._driver, 50).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '#spinner'))
        )
        return self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
