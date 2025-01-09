from CompanyTable import CompanyTable
from CompanyApi import CompanyApi

api = CompanyApi('http://5.101.50.27:8000')
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


# Получение длины списка компании и проверка, что длина списка совпадает с записью в базе данных
def test_get_companies():
    # шаг 1 - получить список через api
    api_result = api.get_company_list()
    # шаг 2 - получить список из БД
    db_result = db.get_companies()
    # шаг 3 - проверить, что списки равны
    assert len(api_result) == len(db_result)


# Сравнить длину списка активных компаний полученных через api с базой данных
def test_get_active_companies():
    # Получить список активных компаний из api
    api_filtered_list = api.get_company_list(params_to_add={'active' : 'true'})
    # Получить список активных компаний из БД
    db_filtered_list = db.get_active_companies()
    # Проверить, что списки равны
    assert len(api_filtered_list) == len(db_filtered_list)

# Создание новой компании и проверка корректности ее создания
def test_add_new():
    # Получить количество компаний через api
    body = api.get_company_list()
    len_before = len(body)
    # создание компании через api
    name = 'Kosta Test'
    descr = 'testing company'
    result = api.create_company(name, descr)
    new_id = result['id']
    # Повторно получить количество компаний
    body = api.get_company_list()
    len_after = len(body)
    # удаление компании из БД
    db.delete(new_id)
    # Проверка разности длины списков
    assert len_after - len_before == 1
    # Так как наш id может быть не последним, нам надо его найти
    # Для этого создадим цикл в котором если найдется компания с нужным id, то будут выполнены проверки
    for company in body:
        if company['id'] == new_id:
            assert company['name'] == name
            assert company['description'] == descr
            assert company['id'] == new_id


# Получение данных новой компании и проверка корректности данных через api
def test_get_one_company():
    # подготовка - создать компанию через БД
    name = 'Kosta SkyPro'
    descr = 'Description Kosta company'
    db.create(name, descr)
    # получить ее id
    new_id = db.get_max_id()
    # главное действие - получение данных компании
    new_company = api.get_company(new_id)
    # постобработка - удаление компании
    db.delete(new_id)
    # проверка полей нашей компании
    assert new_company['id'] == new_id
    assert new_company['name'] == name
    assert new_company['description'] == descr
    assert new_company["is_active"] == True

# Редактирование данных компании и проверка корректности данных через api
def test_edit_company():
    # подготовка - создать компанию через БД
    name = 'Kosta Edit company'
    descr = 'edit me'
    db.create(name, descr)
    new_id = db.get_max_id()
    # изменение компании через api
    new_name = 'Kosta UPDATED'
    new_descr = '__upd__'
    edited = api.edit(new_id, new_name, new_descr)
    # постобработка - удаление компании
    db.delete(new_id)
    # прверка измененных данных
    assert edited['name'] == new_name
    assert edited['description'] == new_descr

# проверка удаления компании: удалили через api, проверили через БД
def test_delete_company():
    # подготовка - создать компанию через БД
    name = 'Kosta Delete company'
    descr = 'delete me'
    db.create(name, descr)
    new_id = db.get_max_id()
    # удаление компании через api
    deleted = api.delete(new_id)
    assert deleted["detail"] == "Компания успешно удалена"
    assert deleted["company_id"] == new_id
    # получение пустой таблицы( id удаленной компании нет)
    rows = db.get_company_by_id(new_id)
    assert len(rows) == 0

def test_company_deactivate():
    name = 'Kosta company to be deactivated'
    descr = 'deactivate me'
    db.create(name, descr)
    new_id = db.get_max_id()
    body = api.deactivate(new_id,False)
    db.delete(new_id)
    assert len(body) == 1
    assert body["is_active"] is False

def test_deactivate_and_activate_back():
    name = 'Kosta company to be deactivated'
    descr = 'deactivate me'
    db.create(name, descr)
    new_id = db.get_max_id()
    api.deactivate(new_id,False)
    body = api.deactivate(new_id, True)
    db.delete(new_id)
    assert body["is_active"] is True

# получене компании по id из БД
def test_get_company_by_id():
    rows = db.get_company_by_id(33)
    assert len(rows) == 1
