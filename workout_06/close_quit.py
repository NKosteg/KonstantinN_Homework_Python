from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# browser.get('https://demoqa.com/browser-windows')
#
# browser.find_element(By.CSS_SELECTOR, '#tabButton').click()

browser.get('https://www.aviasales.ru/')
sleep(2)
browser.find_element(By.CSS_SELECTOR, 'a.s__WJBFOjXpaWb4CntP5Bga').click()
sleep(2)
browser.close()
sleep(5)
browser.quit()
