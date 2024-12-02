from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/ajax')

driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
driver.implicitly_wait(20)

text_on_the_green_bar = driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text
print(text_on_the_green_bar)

driver.quit()
