from YougileApi import YougileAPI

api = YougileAPI("https://yougile.com")
token = "" #Подставь значение


# Получить список, [GET] /api-v2/projects
# Получение списка проектов и проверка, что есть хотя бы один проект
def test_get_list_projects():
    list_project = api.list_of_projects(token)
    assert len(list_project) > 0


# Попытка получения списка проектов без токена авторизации
def test_get_project_negative():
    list_project = api.list_of_projects_negative(token)
    assert list_project["statusCode"] == 401
    assert list_project["message"] == "Unauthorized"


# Создание проекта, [POST] /api-v2/projects
# Создание проекта со всеми заполнеными полями
def test_add_project_with_all_fields():
    list_project = api.list_of_projects(token)
    len_before = len(list_project["content"])
    title = "Мой первый проект"
    users = {
                "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
            }
    project = api.creating_project(token, title, users)
    new_id = project["id"]
    list_project = api.list_of_projects(token)
    len_after = len(list_project["content"])
    assert len_after - len_before == 1
    assert list_project["content"][-1]["id"] == new_id


# Создание проекта с заполненным только обязательным полем (title)
def test_add_project_with_the_required_field():
    list_project = api.list_of_projects(token)
    len_before = len(list_project["content"])
    title = "Проект без администратора"
    project = api.creating_project(token, title)
    new_id = project["id"]
    list_project = api.list_of_projects(token)
    len_after = len(list_project["content"])
    assert len_after - len_before == 1
    assert list_project["content"][-1]["id"] == new_id


# Проверка, что без обязательного поля (title), проект не создан
def test_add_project_negative():
    title = ""
    users = {
        "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
    }
    project = api.creating_project(token, title, users)
    assert project["statusCode"] == 400
    assert project["error"] == "Bad Request"


# Получть проект по  ID, [GET] /api-v2/projects/{id}
# Получение по действительному ID
def test_get_project():
    title = "Мой проект"
    users = {
        "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
    }
    project = api.creating_project(token, title, users)
    new_id = project["id"]
    my_project = api.existing_project(token, new_id)
    my_title = my_project["title"]
    my_user = my_project["users"]["a3dc935a-47b4-4fa6-8aa3-3428dd2e7608"]
    my_id = my_project["id"]
    assert my_title == title
    assert my_user == "admin"
    assert my_id == new_id


# Попытка получить проект с пустым ID
def test_get_project_for_empty_id():
    new_id = " "
    my_project = api.existing_project(token, new_id)
    assert my_project["statusCode"] == 404
    assert my_project["message"] == "Проект не найден"


# Изменение проекта, [PUT] /api-v2/projects/{id}
# Добавление пользователя в проект без администратора
def test_add_admin():
    title = "Проект для добавления администратора"
    project = api.creating_project(token, title)
    new_id = project["id"]

    users = {
        "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
    }
    api.changing_add_admin(token, new_id, users)
    mod_project = api.existing_project(token, new_id)
    my_id = mod_project["id"]
    my_user = mod_project["users"]["a3dc935a-47b4-4fa6-8aa3-3428dd2e7608"]
    assert my_id == new_id
    assert my_user == "admin"


# Изменение названия проекта
def test_title_change_project():
    title = "Мой первый проект до изменения названия"
    users = {
        "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
    }
    project = api.creating_project(token, title, users)
    new_id = project["id"]
    new_title = "Название проекта изменено"
    api.changing_title_project(token, new_id, new_title)
    mod_project = api.existing_project(token, new_id)
    my_id = mod_project["id"]
    my_new_title = mod_project["title"]
    assert my_id == new_id
    assert my_new_title == new_title


# Удаление проекта по ID
def test_delete_project():
    title = "Проект для удаления"
    users = {
        "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
    }
    project = api.creating_project(token, title, users)
    new_id = project["id"]
    deleted_project = api.delete_project(token, new_id)
    project_that_was_deleted = api.existing_project(token, new_id)
    assert deleted_project == 200
    assert project_that_was_deleted["id"] == new_id
    assert project_that_was_deleted["deleted"] is True


# Изменение проекта не указав ID
def test_change_project_for_empty_id():
    title = "Проект, который не изменить без ID"
    users = {
        "a3dc935a-47b4-4fa6-8aa3-3428dd2e7608": "admin"
    }
    api.creating_project(token, title, users)
    new_id = ""
    new_title = "Название проекта изменено"
    mod_project = api.changing_title_project(token, new_id, new_title)
    assert mod_project["statusCode"] == 404
    assert mod_project["error"] == "Not Found"
