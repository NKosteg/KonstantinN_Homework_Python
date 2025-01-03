from selenium.webdriver.common.by import By

class MainPage:


    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get('https://www.labirint.ru/')
        self._driver.implicitly_wait(4)

    def set_cookie_policy(self):
        my_cookie = {
            'name': 'cookie_policy',
            'value': '1'
        }
        self._driver.add_cookie(my_cookie)

    def search(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

