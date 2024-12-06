from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_positive_form():
    #  Открыть страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Заполнить форму значениями
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.clear()
    first_name.send_keys('Иван')
    last_name = driver.find_element(By.NAME, 'last-name')
    last_name.clear()
    last_name.send_keys('Петров')
    address = driver.find_element(By.NAME, 'address')
    address.clear()
    address.send_keys('Ленина, 55-3')
    email = driver.find_element(By.NAME, 'e-mail')
    email.clear()
    email.send_keys('test@skypro.com')
    phone = driver.find_element(By.NAME, 'phone')
    phone.clear()
    phone.send_keys('+7985899998787')
    city = driver.find_element(By.NAME, 'city')
    city.clear()
    city.send_keys('Москва')
    country = driver.find_element(By.NAME, 'country')
    country.clear()
    country.send_keys('Россия')
    job_position = driver.find_element(By.NAME, 'job-position')
    job_position.clear()
    job_position.send_keys('QA')
    company = driver.find_element(By.NAME, 'company')
    company.clear()
    company.send_keys('SkyPro')

    # Нажать кнопку Submit.
    driver.find_element(By.CSS_SELECTOR, 'button').click()

    # Проверить, что поле Zip code подсвечено красным.
    color_zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('color')
    assert color_zip_code == 'rgba(132, 32, 41, 1)'

    # Проверить, что остальные поля подсвечены зеленым.
    color_first_name = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('color')
    assert color_first_name == 'rgba(15, 81, 50, 1)'
    color_last_name = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('color')
    assert color_last_name == 'rgba(15, 81, 50, 1)'
    color_address = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('color')
    assert color_address == 'rgba(15, 81, 50, 1)'
    color_email = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('color')
    assert color_email == 'rgba(15, 81, 50, 1)'
    color_phone = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('color')
    assert color_phone == 'rgba(15, 81, 50, 1)'
    color_city = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('color')
    assert color_city == 'rgba(15, 81, 50, 1)'
    color_country = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('color')
    assert color_country == 'rgba(15, 81, 50, 1)'
    color_job_position = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('color')
    assert color_job_position == 'rgba(15, 81, 50, 1)'
    color_company = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('color')
    assert color_company == 'rgba(15, 81, 50, 1)'
    driver.quit()




