from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get('https://ya.ru')

browser.maximize_window()
sleep(1)
browser.minimize_window()
sleep(1)
browser.fullscreen_window()
sleep(1)
browser.set_window_size(1000, 600)
sleep(5)

browser.quit()
