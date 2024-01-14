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
            vacancy = Vacancy(i["name"], i["salary"], i["alternate_url"], i["area"]["name"], i["employer"]["name"])
            self.vaclist_1.append(vacancy.to_json())
        return self.vaclist_1


class SJConversion(Conversion):
    def for_print(self, data):
        for i in data:
            vacancy = Vacancy(i["profession"], i["payment_from"], i["link"], i["town"]["title"], i["firm_name"])
            self.vaclist_2.append(vacancy.to_json())
        return self.vaclist_2


class PrintHelper:
    def __init__(self):
        self.vac_num = 1
        self.page_num = 1  # Номер страницы (вспомогательная для проги)
        self.vac_on_page = 5  # Кол-во вакансий на одной странице (настравается пользователем)
        self.pages = len(self.data) / self.vac_on_page  # Кол-во страниц

        self.last = self.vac_on_page * self.page_num + 1  # 16 211
        self.first = self.last - self.vac_on_page  # 11 26 311 416 521

    def base_print(self, data):
        for i in data:
            vac = Vacancy(i["name"], i["salary"]["from"], i["link"],  i["region"], i["company"])
            for el in range(self.first, self.last):
                if el == self.vac_num:
                    print(f"{self.vac_num}. {vac}")
            self.vac_num += 1
        self.vac_num = 1

    def qweewq(self, user_action):
        if user_action == "":
            if self.page_num != self.pages:
                self.page_num += 1
                #self.base_print(data)  # Запускай скрипт
        elif user_action == "b":
            if self.page_num != 1:
                self.page_num -= 1
                #self.base_print(data)  # Запускай скрипт
        elif user_action == "df":
            pass  # Запускай скрипт
        elif user_action == "top":
            pass  # Запускай скрипт
        else:
            "Такой команды нет"
            #self.base_print(data)  # Запускай скрипт
