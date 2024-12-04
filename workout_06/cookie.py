from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'

}

browser.get("https://labirint.ru")
browser.add_cookie(my_cookie)

cookie = browser.get_cookie('domain_sid')
print(cookie)

# cookies = browser.get_cookies()
# print(cookies)

# browser.refresh()
# browser.delete_all_cookies()
# browser.refresh()

# sleep(5)
browser.quit()