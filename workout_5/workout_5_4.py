from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver.get("https://www.example.com")
# print(f'Заголовок страницы: {driver.title}')
# sleep(5)
# driver.quit()

# driver.get('https://www.python.org/')
# button_donat = driver.find_element(By.CSS_SELECTOR, 'a.donate-button')
# button_donat.click()
# sleep(5)
# driver.quit()

driver.get('https://www.google.com/')
search_input = driver.find_element(By.CSS_SELECTOR, 'textarea.gLFyf')
search_input.send_keys('Selenium', Keys.RETURN)
sleep(5)
driver.quit()










'textarea.gLFyf'