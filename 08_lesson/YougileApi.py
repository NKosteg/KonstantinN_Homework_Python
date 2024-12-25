import requests


class YougileAPI:
    def __init__(self, url):
        self.url = url

    # Получение списка проектов
    def list_of_projects(self, my_token):
        my_headers = {}
        my_headers["Authorization"] = my_token
        resp = requests.get(self.url + '/api-v2/projects', headers=my_headers)
        return resp.json()

    # Получение списка проектов без токена авторизации
    def list_of_projects_negative(self, my_token):
        resp = requests.get(self.url + '/api-v2/projects')
        return resp.json()

    # Получение проекта по ID
    def existing_project(self, my_token, my_id):
        my_headers = {}
        my_headers["Authorization"] = my_token
        resp = requests.get(self.url + '/api-v2/projects/' + my_id, headers=my_headers)
        return resp.json()

    # Создание проекта
    def creating_project(self, my_token, my_title, my_users=None):
        my_headers = {}
        my_headers["Authorization"] = my_token
        body = {
            "title": my_title,
            "users": my_users
        }
        resp = requests.post(self.url + '/api-v2/projects', headers=my_headers, json=body)
        return resp.json()

    # Изменение проекта: добавление пользователя
    def changing_add_admin(self, my_token, project_id, my_users):
        my_headers = {}
        my_headers["Authorization"] = my_token
        body = {
            "users": my_users
        }
        resp = requests.put(self.url + '/api-v2/projects/' + project_id, headers=my_headers, json=body)
        return resp.json()

    # Изменение проекта: изменение названия
    def changing_title_project(self, my_token, project_id, my_title):
        my_headers = {}
        my_headers["Authorization"] = my_token
        body = {
            "title": my_title
        }
        resp = requests.put(self.url + '/api-v2/projects/' + project_id, headers=my_headers, json=body)
        return resp.json()

    # Удаление проекта
    def delete_project(self, my_token, project_id):
        my_headers = {}
        my_headers["Authorization"] = my_token
        body = {
            "deleted": True
        }
        resp = requests.put(self.url + '/api-v2/projects/' + project_id, headers=my_headers, json=body)
        return resp.status_code
