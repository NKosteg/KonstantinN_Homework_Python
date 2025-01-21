from CompanyApi import CompanyApi

# Получение длины списка компании и проверка, что в нем есть хотя бы одна компания
def test_get_companies(client: CompanyApi):
    body = client.get_company_list()
    assert len(body) > 0

# Сравнить длину списка всех комнаний с длиной списка активных компаний
def test_get_active_companies(client: CompanyApi):
    # Получить список всех компаний
    full_list = client.get_company_list()
    # Получить список активных компаний
    filtered_list = client.get_company_list(params_to_add={'active' : 'true'})
    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

# Создание новой компании и проверка корректности ее создания
def test_add_new(client: CompanyApi):
    # Получить количество компаний
    body = client.get_company_list()
    len_before = len(body)
    # создание
    name = 'Kosta Test'
    descr = 'testing company'
    result = client.create_company(name, descr)
    new_id = result['id']
    # Повторно получить количество компаний
    body = client.get_company_list()
    len_after = len(body)
    # Проверки
    assert len_after - len_before == 1
    assert body[-1]['name'] == name
    assert body[-1]['description'] == descr
    assert body[-1]['id'] == new_id

# Получение данных новой компании
def test_get_one_company(client: CompanyApi):
    name = 'Kosta Test'
    descr = 'testing company'
    result = client.create_company(name, descr)
    new_id = result['id']

    new_company = client.get_company(new_id)
    assert new_company['id'] == new_id
    assert new_company['name'] == name
    assert new_company['description'] == descr
    assert new_company["is_active"] == True
# Редактирование данных компании
def test_edit_company(client: CompanyApi):
    name = 'Kosta Edit company'
    descr = 'edit me'
    result = client.create_company(name, descr)
    new_id = result['id']
    print(result)

    new_name = 'Kosta UPDATED'
    new_descr = '__upd__'
    edited = client.edit(new_id, new_name, new_descr)
    assert edited['name'] == new_name
    assert edited['description'] == new_descr
    print(edited)

 # Авторизация(получение токена)
def test_get_auth(client: CompanyApi):
    result = client.get_token()
    print(result)

def test_delete_company(client: CompanyApi):
    name = 'Kosta company to be deleted'
    descr = 'delete me'
    result = client.create_company(name, descr)
    new_id = result['id']

    new_company = client.get_company(new_id)
    assert new_company['name'] == name
    assert new_company['description'] == descr
    assert new_company["is_active"] is True

    deleted = client.delete(new_id)
    assert deleted["detail"] == "Компания успешно удалена"
    assert deleted["company_id"] == new_id

    full_list = client.get_company_list()
    assert full_list[-1]['id'] != new_id

def test_company_deactivate(client: CompanyApi):
    name = 'Kosta company to be deactivated'
    descr = 'deactivate me'
    result = client.create_company(name, descr)
    new_id = result['id']
    body = client.deactivate(new_id,False)
    assert len(body) == 1
    assert body["is_active"] is False

def test_deactivate_and_activate_back(client: CompanyApi):
    name = 'Kosta company to be deactivated'
    descr = 'deactivate me'
    result = client.create_company(name, descr)
    new_id = result['id']
    client.deactivate(new_id,False)
    body = client.deactivate(new_id, True)
    assert body["is_active"] is True
