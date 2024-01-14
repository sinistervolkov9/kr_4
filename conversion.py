from abc import ABC, abstractmethod
from vacancy import Vacancy


class Conversion(ABC):
    somelist_1 = []
    somelist_2 = []
    @abstractmethod
    def for_print(self, data):
        pass


class HHConversion(Conversion):
    def for_print(self, data):
        for i in data:
            vacancy = Vacancy(i["name"], i["salary"], i["alternate_url"], i["area"]["name"], i["employer"]["name"])
            self.somelist_1.append(vacancy.to_json())
        return self.somelist_1


class SJConversion(Conversion):
    def for_print(self, data):
        for i in data:
            vacancy = Vacancy(i["profession"], i["payment_from"], i["link"], i["town"]["title"], i["firm_name"])
            self.somelist_2.append(vacancy.to_json())
        return self.somelist_2
