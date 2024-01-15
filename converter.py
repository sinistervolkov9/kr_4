from abc import ABC, abstractmethod
from vacancy import Vacancy


class Conversion(ABC):
    vaclist_1 = []
    vaclist_2 = []

    @abstractmethod
    def for_print(self, data):
        pass


class HHConversion(Conversion):
    def for_print(self, data):
        for i in data:
            if i["salary"] is not None:
                if "from" in i["salary"]:
                    salary_from = i["salary"]["from"]
                    if salary_from == None:
                        salary_from = "не указано"
                else:
                    salary_from = "не указано"
            else:
                salary_from = "не указано"
            vacancy = Vacancy(i["name"], salary_from, i["alternate_url"], i["area"]["name"], i["employer"]["name"])
            self.vaclist_1.append(vacancy.to_json())
        return self.vaclist_1


class SJConversion(Conversion):
    def for_print(self, data):
        for i in data:
            vacancy = Vacancy(i["profession"], i["payment_from"], i["link"], i["town"]["title"], i["firm_name"])
            self.vaclist_2.append(vacancy.to_json())
        return self.vaclist_2
