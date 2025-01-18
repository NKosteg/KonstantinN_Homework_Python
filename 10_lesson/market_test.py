import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from AuthorizPage import AuthorizationPage
from ProductsPage import ProductsPage
from InformPage import InformationPage
from TotalPage import TotalPage


@pytest.fixture()
def driver():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Развернуть окно на максимальный размер"):
        browser.maximize_window()
    yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.suite("Маркет")
@allure.title("Работа с корзиной.")
@allure.description("Добавление товаров в корзину с последующей проверкой общей суммы находящихся там товаров авторизованным пользователем.")
@allure.feature("READ")
@allure.severity("Critical")
def test_market_cart(driver):
    with allure.step("Открыть страницу маркета"):
        login = AuthorizationPage(driver)
        login.authorization('standard_user', 'secret_sauce')
    with allure.step("Перейти к товарам"):
        products = ProductsPage(driver)
        products.add_products()
    with allure.step("Перейти к оформлению"):
        information = InformationPage(driver)
        information.your_information()
    with allure.step("Проверить сумму товаров на соответствие"):
        total = TotalPage(driver)
        result = total.cart_total()
        with allure.step("Проверить, что сумма равна $58.29"):
            assert result == 'Total: $58.29'
