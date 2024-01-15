import requests
from abc import ABC, abstractmethod
from settings import SUPERJOB_API_KEY


class Api(ABC):
    """
    Класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_request(self, keyword, per_page):
        pass


class HHAPI(Api):
    """
    Класс для работы конкретно с платформой hh.ru
    """

    def get_request(self, keyword, per_page=100):
        url = "https://api.hh.ru/vacancies/"
        params = {"text": keyword, "search_field": "name", "page": 0, "per_page": per_page}

        request = requests.get(url, params=params)
        return request.json()["items"]


class SuperjobAPI(Api):
    """
    Класс для работы конкретно с платформой superjob.ru
    """

    def get_request(self, keyword, per_page=100):
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {"keywords": keyword, "page": 0, "count": per_page}

        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        request = requests.get(url, params=params, headers=headers)
        return request.json()["objects"]
