from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

def open_google():
    browser.maximize_window()
    browser.get('https://www.google.com/')
    browser.implicitly_wait(5)

def search_google(term):
    browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(term, Keys.RETURN)

def get_search_result():
    return browser.find_elements(By.CSS_SELECTOR, 'div.g')




def close_browser():
    browser.quit()

def test_search_google():
    open_google()
    search_google('Selenium Python')
    get_search_result()
    sleep(5)
    close_browser()
    # assert len(get_search_result()) > 0, 'Результаты поиска не найдены.'





