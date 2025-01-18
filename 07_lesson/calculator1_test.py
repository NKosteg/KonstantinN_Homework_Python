import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalcPage import CalculatorPage


@pytest.fixture()
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()


def test_calculator(driver):
    sum_of_numbers = CalculatorPage(driver)
    sum_of_numbers.input_delay('45')
    sum_of_numbers.press_buttons()
    result = sum_of_numbers.output_result()
    assert result == '15'
