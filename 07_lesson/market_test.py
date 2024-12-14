import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from pages.AuthorizPage import AuthorizationPage
from pages.ProductsPage import ProductsPage
from pages.InformPage import InformationPage
from pages.TotalPage import TotalPage


@pytest.fixture()
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    browser.quit()


def test_market_cart(driver):
    login = AuthorizationPage(driver)
    login.authorization('standard_user', 'secret_sauce')
    products = ProductsPage(driver)
    products.add_products()
    information = InformationPage(driver)
    information.your_information()
    total = TotalPage(driver)
    result = total.cart_total()
    assert result == 'Total: $58.29'
