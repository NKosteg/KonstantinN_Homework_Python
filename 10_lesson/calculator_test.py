import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from CalcPage import CalculatorPage


@pytest.fixture()
def driver():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.suite("Калькулятор")
@allure.title("Задержка в вычислениях калькулятора.")
@allure.description("Проверка вычислений суммы двух чисел, при заданной задержке обработки операции.")
@allure.feature("READ")
@allure.severity("Blocker")
def test_calculator(driver):
    with allure.step("Отккрыть приложение калькулятор"):
        sum_of_numbers = CalculatorPage(driver)
    sum_of_numbers.input_delay('5')
    with allure.step("Произвести вычисления"):
        sum_of_numbers.press_buttons()
    with allure.step("Дождаться результата"):
        result = sum_of_numbers.output_result()
    with allure.step("Сравнить результат с ожидаемым"):
        assert result == '15'
