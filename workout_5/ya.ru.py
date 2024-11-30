
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.get("https://ya.ru")
driver.get("https://vk.com")

for x in range(1, 3):
    driver.back()
    sleep(1)
    driver.forward()
    sleep(1)

driver.refresh()

driver.set_window_size(640, 480)
sleep(2)
driver.fullscreen_window()
sleep(1)

driver.save_screenshot('./ya.png')
# sleep(5)
