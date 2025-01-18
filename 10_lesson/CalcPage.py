from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        with allure.step("Развернуть окно на максимальный размер"):
            self._driver.maximize_window()
        with allure.step("Перейти на страницу с кальклятором"):
            self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    @allure.step("Выставить таймер задержки выполнения операции {time}")
    def input_delay(self, time: str) -> None:
        input_delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        input_delay.clear()
        input_delay.send_keys(time)

    def press_buttons(self) -> None:
        with allure.step("Нажать кнопку с цифрой '7'"):
            self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        with allure.step("Нажать кнопку со знаком '+'"):
            self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        with allure.step("Нажать кнопку с цифрой '8'"):
            self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        with allure.step("Нажать кнопку со знаком '='"):
            self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def output_result(self) -> str:
        WebDriverWait(self._driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '#spinner'))
        )
        return self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
