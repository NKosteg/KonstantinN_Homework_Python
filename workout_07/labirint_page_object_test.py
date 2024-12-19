from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPages import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('python')

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get_cart()
    as_is = cart_page.get_counter()

    assert as_is == to_be

    browser.quit()


def test_empty_search_result():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search(' ')

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    assert msg == 'Все, что мы нашли в Лабиринте по запросу «»'
    browser.quit()
