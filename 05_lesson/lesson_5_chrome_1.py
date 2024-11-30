from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
sleep(1)
# Пять раз кликните на кнопку Add Element
add_element = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
for i in range(5):
    add_element.click()
sleep(1)
# Соберите со страницы список кнопок Delete
elements = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

# Выведите на экран размер списка.
print(f'Размер списка: {len(elements)} элементов.')

driver.quit()



