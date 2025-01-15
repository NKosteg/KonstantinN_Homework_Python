from selenium.webdriver.common.by import By
import allure


class FormPage:
    def __init__(self, driver):
        self._driver = driver
        with allure.step("Развернуть окно на максимальный размер"):
            self._driver.maximize_window()
        with allure.step("Перейти на страницу с формой"):
            self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        with allure.step("Подождать загрузки страницы, не более 4-х секунд"):
            self._driver.implicitly_wait(4)

    @allure.step("Заполнить поле {selector} данными {data}")
    def input_value(self, selector: str, data: str) -> None:
        text_input_field = self._driver.find_element(By.NAME, selector)
        text_input_field.clear()
        text_input_field.send_keys(data)

    @allure.step("Нажать кнопку 'Submit")
    def button_click(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, 'button').click()

    @allure.step("Проверка заполненного поля по {id_element}")
    def checking_input(self, id_element: str) -> str:
        return self._driver.find_element(By.CSS_SELECTOR, id_element).value_of_css_property('color')

    @allure.step("Проверка не заполненного поля по {id_element}")
    def checking_empty_input(self, id_element: str) -> str:
        return self._driver.find_element(By.CSS_SELECTOR, id_element).value_of_css_property('color')
