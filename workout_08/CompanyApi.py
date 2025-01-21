import requests

class CompanyApi:

    def __init__(self, url):
        self.url = url
        self.params = {"client_token": self.get_token()}

    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        return resp.json()

    def get_token(self, user='harrypotter', password='expelliarmus'):
        print("Auth")
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['user_token']

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        # my_headers={}
        # my_headers["client_token"] = self.get_token()
        resp = requests.post(self.url + '/company/create', json=company)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    def edit(self, new_id, new_name, new_descr):
        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + '/company/update/' + str(new_id), params=self.params, json=company)
        # Либо
        # client_token = self.get_token()
        # resp = requests.patch(f"{self.url}/company/update/{new_id}?self.params, json=company)
        return resp.json()

    def delete(self, id):
        resp =requests.delete(self.url + '/company/' + str(id), params=self.params)
        return resp.json()

    def deactivate(self, id, status):

        resp = requests.patch(self.url + '/company/status_update/' + str(id), params=self.params, json={"is_active": status})
        return resp.json()
