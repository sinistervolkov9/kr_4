import os
from pip._vendor import requests
from settings import HH_API_KEY, SUPERJOB_API_KEY

# Создать абстрактный класс для работы с API сайтов с вакансиями.
class Api:
    """
    абстрактный класс для работы с API сайтов с вакансиями.
    """
    def get_request(self):
        pass


# Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами.
class HH(Api):
    def __init__(self, keyword, page=1):
        self.url = "https://api.hh.ru/vacancies/"
        self.params = {"text": keyword, "page": page, "per_page": 50, "search_field": "name"}

    def get_request(self):
        request = requests.get(self.url, params=self.params)
        return request


class Superjob(Api):
    def __init__(self, keyword, page=0):
        self.url = "https://api.syperjob.ru/2.0/vacancies/"
        self.params = {"keywords[0][keys]": keyword, "page": page, "count": 50}

    def get_request(self):
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        return requests.get(self.url, headers=headers, params=self.params)

# Классы должны уметь подключаться к API и получать вакансии.
