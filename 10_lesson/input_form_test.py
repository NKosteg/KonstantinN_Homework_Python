import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from FormPage import FormPage


@pytest.fixture()
def driver():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.suite("Форма")
@allure.title("Заполнение формы.")
@allure.description("Проверка того, что заполненные поля формы подсвечены зеленым цветом, а незаполненные - красным.")
@allure.feature("CREATE")
@allure.severity("Trivial")
def test_form_input(driver):
    with allure.step("Открыть страницу формы"):
        form_page = FormPage(driver)
    with allure.step("Заполнить поля формы"):
        form_page.input_value("first-name", 'Иван')
        form_page.input_value('last-name', 'Петров')
        form_page.input_value('address', 'Ленина, 55-3')
        form_page.input_value('e-mail', 'test@skypro.com')
        form_page.input_value('phone', '+7985899998787')
        form_page.input_value('city', 'Москва')
        form_page.input_value('country', 'Россия')
        form_page.input_value('job-position', 'QA')
        form_page.input_value('company', 'SkyPro')
    form_page.button_click()
    id_elements = ['#first-name', '#last-name', '#address', '#e-mail', '#phone', '#city', '#country', '#job-position', '#company']
    with allure.step("Проверка заполненных полей"):
        for id_element in id_elements:
            color_field = form_page.checking_input(id_element)
            with allure.step("Поле подсвечено зеленым"):
                assert color_field == 'rgba(15, 81, 50, 1)'
    color_zip_code = form_page.checking_empty_input('#zip-code')
    with allure.step("Поле подсвечено красным"):
        assert color_zip_code == 'rgba(132, 32, 41, 1)'
