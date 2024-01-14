import sys
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
    def __init__(self, data):
        self.vac_on_page = 5  # Кол-во вакансий на одной странице (настравается пользователем)
        self.data = data
        self.run = True

        self.page_num = 1  # Номер страницы (вспомогательная для проги)
        self.pages = len(self.data) // self.vac_on_page  # Кол-во страниц

    def base_print(self):
        vac_num = 1
        last = self.vac_on_page * self.page_num + 1  # 16 211
        first = last - self.vac_on_page  # 11 26 311 416 521

        for i in self.data:
            vac = Vacancy(i["name"], i["salary"], i["link"],  i["region"], i["company"])
            for element in range(first, last):
                if element == vac_num:
                    print(f"{vac_num}. {vac}")
            vac_num += 1
        print(f"\nСтраница {self.page_num} из {int(self.pages)}")

    def check_quit(self):
        if self.run is True:
            self.base_print()
        else:
            sys.exit()

    def response_handler(self, user_action):
        if user_action == "":
            if self.page_num != self.pages:
                self.page_num += 1
            self.check_quit()
        elif user_action == "b":
            if self.page_num != 1:
                self.page_num -= 1
            self.check_quit()
        elif user_action == "df":
            pass  # Запускай скрипт. Функция, в которую надо будет передать список значений
        elif user_action == "top":
            pass  # Запускай скрипт. Функция, в которую надо будет передать 1 значение
        elif user_action == "dl":
            pass  # Запускай скрипт. Функция, в которую надо будет передать список значений
        elif user_action == "e":
            self.run = False
            self.check_quit()
        else:
            print("Такой команды нет\n")
            self.check_quit()

















































