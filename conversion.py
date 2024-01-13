from abc import ABC, abstractmethod
from vacancy import Vacancy
from record import Record


class Conversion(ABC):
    @abstractmethod
    def preparing_for_json(self, items, record, resource_list):
        pass


class HHConversion(Conversion):
    def preparing_for_json(self, items, record, resource_list):
        for i in items:
            vacancy = Vacancy(i["name"], i["salary"]["from"], i["alternate_url"], i["area"]["name"], i["employer"]["name"])
            record.to_add_data(vacancy.to_json())
        resource_list.append(record)


class SJConversion(Conversion):
    def preparing_for_json(self, items, record, resource_list):
        for i in items:
            vacancy = Vacancy(i["profession"], i["payment_from"], i["link"], i["town"]["title"], i["firm_name"])
            record.to_add_data(vacancy.to_json())
        resource_list.append(record)
