import requests


class employee_api:
    def __init__(self, url):
        """инициализация

        Args:
            url (_type_): _description_
        """
        self.url = url
        
        
    def get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
        
    def get_company_id(self, name = 'great_company', description = 'desc'):
        """создание новой компании, для получения id

        Args:
            name (str, optional): _description_. Defaults to 'great_company'.
            description (str, optional): _description_. Defaults to 'desc'.

        Returns:
            _type_: _description_
        """
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json = company, headers = my_headers)
        return resp.json()["id"]
    
    
    def get_employee(self, id):
        """Получить список сотрудников компании

        Args:
            id (_type_): _description_

        Returns:
            _type_: _description_
        """
        resp = requests.get(self.url + '/employee?company=' + str(id))
        return resp
    
    
    def post_employee(self, id, em_id = 1, fname = 'cool_first_name', lname = 'cool_last_name', mname = 'cool_middle_name', email = 'great_e@mail.com', eurl = 'smth', phone = '88005553535', birthdate = '2024-05-14T19:16:21.649Z'):
        """Добавить нового сотрудника

        Args:
            id (_type_): _description_
            em_id (int, optional): _description_. Defaults to 1.
            fname (str, optional): _description_. Defaults to 'cool_first_name'.
            lname (str, optional): _description_. Defaults to 'cool_last_name'.
            mname (str, optional): _description_. Defaults to 'cool_middle_name'.
            email (str, optional): _description_. Defaults to 'great_e@mail.com'.
            eurl (str, optional): _description_. Defaults to 'smth'.
            phone (str, optional): _description_. Defaults to '88005553535'.
            birthdate (str, optional): _description_. Defaults to '2024-05-14T19:16:21.649Z'.

        Returns:
            _type_: _description_
        """
        creds = {
           "id": em_id,
            "firstName": fname,
            "lastName": lname,
            "middleName": mname,
            "companyId": id,
            "email": email,
            "url": eurl,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": True 
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json = creds, headers = my_headers)
        return resp
    
        
    def get_employee_by_id(self, em_id):
        """Полкчить сотрудника по id

        Args:
            em_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        resp = requests.get(self.url + '/employee/' + str(em_id))
        return resp
    
    
    def patch_employee(self, em_id, email = "someg@gmail.com", eurl = "smthg else"):
        """Изменить информацию о оструднике

        Args:
            em_id (_type_): _description_
            email (str, optional): _description_. Defaults to "someg@gmail.com".
            eurl (str, optional): _description_. Defaults to "smthg else".

        Returns:
            _type_: _description_
        """
        creds = {
            "lastName": 'cool_last_name',
            "email": email,
            "url": eurl,
            "phone": "88005553535",
            "isActive": False
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(em_id), json = creds, headers = my_headers)
        return resp
    
    def delete_company(self, id):
        """удаление компании в конце теста

        Args:
            id (_type_): _description_

        Returns:
            _type_: _description_
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers = my_headers)
        return resp