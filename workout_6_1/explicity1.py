from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get('https://the-internet.herokuapp.com/')
waiter = WebDriverWait(driver, 4)

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[href="/abtest"]'), 'A/B Testing')
)
is_display = driver.find_element(By.CSS_SELECTOR, '[href="/abtest"]').is_displayed()
print(is_display)
sleep(2)

driver.quit()