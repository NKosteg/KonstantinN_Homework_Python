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


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()

    # перейти на сайт лабиринт
    browser.get('https://www.labirint.ru/')
    browser.implicitly_wait(4)
    browser.add_cookie(my_cookie)

    # найти все книги по слову
    browser.find_element(By.CSS_SELECTOR, '#search-field').send_keys('python')
    browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    # добавить все книги в корзину, и посчитать сколько
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    print(counter)
    # перейти в корзину
    browser.get('https://www.labirint.ru/cart/')
    # проверить счетчик товаров. должен быть равен количеству нажатий.
    txt = browser.find_element(By.CSS_SELECTOR, '.j-cart-count').text
    print(txt)
    assert counter == int(txt)
    sleep(5)


    browser.quit()