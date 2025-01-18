import allure
import requests

class CompanyApi:
    """Клас предоставляет методы для работы с сервером приложеня"""

    def __init__(self, url):
        self.url = url

    @allure.step("API.Получить список компаний")
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        return resp.json()

    @allure.step("API.Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['user_token']

    @allure.step("API.Создать компанию {name} ({description})")
    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        # my_headers={}
        # my_headers["client_token"] = self.get_token()
        resp = requests.post(self.url + '/company/create', json=company)
        return resp.json()

    @allure.step("API.Получить компанию по {id}")
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    @allure.step("API.Редактировать компанию {new_id}. {new_name} {new_descr}")
    def edit(self, new_id, new_name, new_descr):
        my_params = {}
        my_params["client_token"] = self.get_token()
        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + '/company/update/' + str(new_id), params=my_params, json=company)
        # Либо
        # client_token = self.get_token()
        # resp = requests.patch(f"{self.url}/company/update/{new_id}?client_token={client_token}", json=company)
        return resp.json()

    @allure.step("API.Удалить компанию {id}")
    def delete(self, id):
        my_params = {}
        my_params["client_token"] = self.get_token()
        resp =requests.delete(self.url + '/company/' + str(id), params=my_params)
        return resp.json()

    @allure.step("API.(Де)Активировать компанию {id} -> {status}")
    def deactivate(self, id, status):
        my_params = {}
        my_params["client_token"] = self.get_token()

        resp = requests.patch(self.url + '/company/status_update/' + str(id), params=my_params, json={"is_active": status})
        return resp.json()
