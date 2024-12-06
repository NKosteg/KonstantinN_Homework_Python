from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 50)

def test_calculator():
    # Открыть страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    # В поле ввода по локатору #delay ввести значение 45
    input_delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    input_delay.clear()
    input_delay.send_keys('45')
    # Нажать кнопки: 7; +; 8; =;
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
    # Дождаться, когда закончит работать прелоадер, и в поле появится результат вычисления
    waiter.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '#spinner'))
    )
    # Вывевсти результат и сравнитьс ожидаемым результатом
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert result == '15'
    driver.quit()
