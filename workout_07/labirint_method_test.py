from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def open_labirint():
    # перейти на сайт лабиринт
    browser.maximize_window()
    browser.get('https://www.labirint.ru/')
    browser.implicitly_wait(4)
    browser.add_cookie(my_cookie)

def search(term):
    # найти все книги по слову
    browser.find_element(By.CSS_SELECTOR, '#search-field').send_keys(term)
    browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

def add_books():
    # добавить все книги в корзину, и посчитать сколько
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
        return counter

def go_to_cart():
    # перейти в корзину
    browser.get('https://www.labirint.ru/cart/')

def get_cart_counter():
    # проверить счетчик товаров.
    txt = browser.find_element(By.CSS_SELECTOR, '.j-cart-count').text
    return int(txt)

def close_browser():
    browser.quit()


def test_cart_counter():
    open_labirint()
    search('python')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_browser()
    assert added == cart_counter
