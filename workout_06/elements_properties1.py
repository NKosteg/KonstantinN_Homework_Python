from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser.get('http://uitestingplayground.com/visibility')
#
# is_displayed = browser.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# print(is_displayed)
# sleep(3)
# browser.find_element(By.CSS_SELECTOR, '#hideButton').click()
# sleep(3)
# is_displayed = browser.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# print(is_displayed)
# sleep(3)

# browser.get('https://demoqa.com/radio-button')
# is_enabled = browser.find_element(By.CSS_SELECTOR,'#yesRadio').is_enabled()
# print(is_enabled)
#
# is_enabled = browser.find_element(By.CSS_SELECTOR,'#noRadio').is_enabled()
# print(is_enabled)

browser.get('https://the-internet.herokuapp.com/checkboxes')
# cb = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
# is_selected = cb.is_selected()
# print(is_selected)
# sleep(2)
#
# cb.click()
# is_selected = cb.is_selected()
# print(is_selected)
# sleep(3)

# div = browser.find_element(By.CSS_SELECTOR, '#page-footer')
# a = div.find_element(By.CSS_SELECTOR, "a")
# print(a.get_attribute('href'))

divs = browser.find_elements(By.CSS_SELECTOR, 'div')
l = len(divs)
print(l)
div = divs[6]
css_class = div.get_attribute('class')
print(css_class)
sleep(3)

browser.quit()