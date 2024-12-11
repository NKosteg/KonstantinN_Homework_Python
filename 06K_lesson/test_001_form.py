import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Параметризировать функцию значениями для формы
@pytest.mark.parametrize('selector, data, id_element', [
    ("first-name", 'Иван', '#first-name'),
    ('last-name', 'Петров', '#last-name'),
    ('address', 'Ленина, 55-3', '#address'),
    ('e-mail', 'test@skypro.com', '#e-mail'),
    ('phone', '+7985899998787', '#phone'),
    ('city', 'Москва', '#city'),
    ('country', 'Россия', '#country'),
    ('job-position', 'QA', '#job-position'),
    ('company', 'SkyPro', '#company')
])
def test_form_positive(selector, data, id_element):
    #  Открыть страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    # Заполнить форму значениями
    text_input_field = driver.find_element(By.NAME, selector)
    text_input_field.clear()
    text_input_field.send_keys(data)
    # Нажать кнопку Submit.
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    # Проверить, что поля подсвечены зеленым.
    color_field = driver.find_element(By.CSS_SELECTOR, id_element).value_of_css_property('color')
    assert color_field == 'rgba(15, 81, 50, 1)'


def test_form_negative():
    #  Открыть страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    # Поле Zip code оставить пустым
    # Нажать кнопку Submit.
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    # Проверить, что поле Zip code подсвечено красным.
    color_zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('color')
    assert color_zip_code == 'rgba(132, 32, 41, 1)'
