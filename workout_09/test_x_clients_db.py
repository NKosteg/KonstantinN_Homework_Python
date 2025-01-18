import allure
from CompanyTable import CompanyTable
from CompanyApi import CompanyApi

@allure.epic('Компании')
@allure.severity('BLOCKER')
@allure.suite('Тесты на работу с организациями')
class TestCompany:

    api = CompanyApi('http://5.101.50.27:8000')
    db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


    # Получение длины списка компании и проверка, что длина списка совпадает с записью в базе данных
    @allure.id('SKYPRO-1')
    @allure.story('Получение компаний')
    @allure.feature('READ')
    @allure.title('Получение полного списка всех существующих организаций')
    def test_get_companies(self):
        api_result = self.api.get_company_list()
        db_result = self.db.get_companies()
        with allure.step("проверить, что списки равны"):
            assert len(api_result) == len(db_result)


    # Сравнить длину списка активных компаний полученных через api с базой данных
    @allure.id('SKYPRO-2')
    @allure.story('Получение активных компаний')
    @allure.feature('READ')
    @allure.title('Получение полного списка всех активных организаций')
    @allure.description('Запрос на получение списка организаций с параметром active = true')
    @allure.severity('MINOR')
    def test_get_active_companies(self):
        # Получить список активных компаний из api
        api_filtered_list = self.api.get_company_list(params_to_add={'active' : 'true'})
        # Получить список активных компаний из БД
        db_filtered_list = self.db.get_active_companies()
        # Проверить, что списки равны
        assert len(api_filtered_list) == len(db_filtered_list)

    # Создание новой компании и проверка корректности ее создания
    @allure.id('SKYPRO-3')
    @allure.story('Создание новой компании')
    @allure.feature('CREATE')
    @allure.title("Создание конкретной организации")
    def test_add_new(self):
        body = self.api.get_company_list()
        len_before = len(body)
        with allure.step("Создать организацию"):
            with allure.step("Сгенерировать данные"):
                name = 'Kosta Test'
                descr = 'testing company'
            result = self.api.create_company(name, descr)
            new_id = result['id']
        body = self.api.get_company_list()
        len_after = len(body)
        self.db.delete(new_id)
        with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ на 1"):
            assert len_after - len_before == 1
        with allure.step("Проверить поля созданной организации на корректность заполнения полей"):
            for company in body:
                if company['id'] == new_id:
                    assert company['name'] == name
                    assert company['description'] == descr
                    assert company['id'] == new_id


    # Получение данных новой компании и проверка корректности данных через api
    @allure.id('SKYPRO-4')
    @allure.story('Получение компании по id')
    @allure.feature('GET')
    @allure.title("Получение данных об организации по id")
    def test_get_one_company(self):
        # подготовка - создать компанию через БД
        name = 'Kosta SkyPro'
        descr = 'Description Kosta company'
        self.db.create(name, descr)
        # получить ее id
        new_id = self.db.get_max_id()
        # главное действие - получение данных компании
        new_company = self.api.get_company(new_id)
        # постобработка - удаление компании
        self.db.delete(new_id)
        # проверка полей нашей компании
        assert new_company['id'] == new_id
        assert new_company['name'] == name
        assert new_company['description'] == descr
        assert new_company["is_active"] == True

    #Редактирование данных компании и проверка корректности данных через api
    def test_edit_company(self):
        # подготовка - создать компанию через БД
        name = 'Kosta Edit company'
        descr = 'edit me'
        self.db.create(name, descr)
        new_id = self.db.get_max_id()
        # изменение компании через api
        new_name = 'Kosta UPDATED'
        new_descr = '__upd__'
        edited = self.api.edit(new_id, new_name, new_descr)
        # постобработка - удаление компании
        self.db.delete(new_id)
        # прверка измененных данных
        assert edited['name'] == new_name
        assert edited['description'] == new_descr

    # проверка удаления компании: удалили через api, проверили через БД
    def test_delete_company(self):
        # подготовка - создать компанию через БД
        name = 'Kosta Delete company'
        descr = 'delete me'
        self.db.create(name, descr)
        new_id = self.db.get_max_id()
        # удаление компании через api
        deleted = self.api.delete(new_id)
        assert deleted["detail"] == "Компания успешно удалена"
        assert deleted["company_id"] == new_id
        # получение пустой таблицы( id удаленной компании нет)
        rows = self.db.get_company_by_id(new_id)
        assert len(rows) == 0

    def test_company_deactivate(self):
        name = 'Kosta company to be deactivated'
        descr = 'deactivate me'
        self.db.create(name, descr)
        new_id = self.db.get_max_id()
        body = self.api.deactivate(new_id,False)
        self.db.delete(new_id)
        assert len(body) == 1
        assert body["is_active"] is False

    def test_deactivate_and_activate_back(self):
        name = 'Kosta company to be deactivated'
        descr = 'deactivate me'
        self.db.create(name, descr)
        new_id = self.db.get_max_id()
        self.api.deactivate(new_id,False)
        body = self.api.deactivate(new_id, True)
        self.db.delete(new_id)
        assert body["is_active"] is True

    # получене компании по id из БД
    def test_get_company_by_id(self):
        rows = self.db.get_company_by_id(33)
        assert len(rows) == 1
