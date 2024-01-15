import math
from vacancy import Vacancy


class PrintHelper:
    """
    Класс для красивого выводода текста в терминале
    """

    def __init__(self, data):
        self.run = True
        self.data = data
        self.vac_on_page = 5  # Кол-во вакансий на одной странице
        self.page_num = 1  # Вспомогательная. Номер страницы
        self.pages = math.ceil(len(self.data) / self.vac_on_page)  # Кол-во страниц
        self.vac_sum = len(self.data)  # Кол-во вакансий

    def base_print(self):
        """
        Обычный базовый вывод страницы с вакансиями,
        в зависимости от номера страницы, их количества,
        количества выводимых вакансий
        :return: None
        """
        vac_num = 1  # Вспомогательная
        last = self.vac_on_page * self.page_num + 1  # Вспомогательная. Последняя выводимая вакансия
        first = last - self.vac_on_page  # Вспомогательная. первая выводимая вакансия

        for i in self.data:
            vac = Vacancy(i["name"], i["salary"], i["link"], i["region"], i["company"])
            for element in range(first, last):
                if element == vac_num:
                    print(f"{vac_num}. {vac}")
            vac_num += 1
        print(f"Всего вакансий - {len(self.data)}")
        print(f"\nСтраница {self.page_num} из {int(self.pages)}")

    def top_print(self, value):
        filtered_data = [i for i in self.data if isinstance(i["salary"], (int, float))]
        filtered_data.sort(key=lambda x: x["salary"], reverse=True)
        vac_num = 1
        for i in filtered_data:
            vac = Vacancy(i["name"], i["salary"], i["link"], i["region"], i["company"])
            if vac_num <= int(value):
                print(f"{vac_num}. {vac}")
                vac_num += 1
            else:
                break
        if len(filtered_data) < len(self.data):
            print("Зарплата некоторых вакансий неизвестна")
        self.to_return()

    def comp_print(self, choice_list):  # [1, 2] -> [2, 3]
        if len(choice_list) < 2:
            print("Для сравнения нужно указать хотя бы две вакансии\n")
        else:
            choiced_vac_list = []
            result = ""
            for i in range(len(choice_list) - 1):
                first = self.data[choice_list[i] - 1]
                second = self.data[choice_list[i + 1] - 1]
                if first not in choiced_vac_list or second not in choiced_vac_list:
                    result += f"{first['name']} - {first['salary']} - {first['region']} "
                    if isinstance(first['salary'], (int, float)):
                        if isinstance(second['salary'], (int, float)):
                            if first['salary'] > second['salary']:
                                result += "> "
                            elif first['salary'] < second['salary']:
                                result += "< "
                            else:
                                result += "= "
                        else:
                            result += "?зарплата одной из вакансий неизвестна? "
                    else:
                        result += "?зарплата одной из вакансий неизвестна? "
                    choiced_vac_list.append(first)
                    result += f"{second['name']} - {second['salary']} - {second['region']}\n"
                    choiced_vac_list.append(second)

            print(result)

        self.to_return()

    def next_page(self):
        if self.page_num != self.pages:
            self.page_num += 1
        self.base_print()

    def previous_page(self):
        if self.page_num != 1:
            self.page_num -= 1
        self.base_print()

    def comparison_vac(self):
        choice_list = []
        print("Введите номера вакансий, которые хотите сравнить (через пробел)")
        user_choice = input().split()
        for i in user_choice:
            if isinstance(i, int) or i.isdigit():
                if 0 < int(i) < int(self.vac_sum):
                    number = int(i)
                    choice_list.append(number)
                else:
                    print(f"Вакансии с номером {i} нет")
            else:
                print(f"Вакансии с номером {i} нет")
        self.comp_print(choice_list)

    def top_vac(self):
        print("Введите значение, сколько вакансий отобразить")
        user_choice = input().strip()
        if isinstance(user_choice, int) or user_choice.isdigit():
            self.top_print(user_choice)
        else:
            print(f"Нужно ввести числовое значение\n")
            self.base_print()

    def remove_vac(self):
        choice_list = []
        print("Введите номера вакансий, которые хотите удалить (через пробел)")
        user_choice = input().split()
        for i in user_choice:
            if isinstance(i, int) or i.isdigit():
                number = int(i)
                choice_list.append(number)
            else:
                print(f"{i} - это не число\n")
        return choice_list

    def no_comand(self):
        print("Такой команды нет\n")
        self.base_print()

    def to_return(self):
        print(f"\nЧтобы вернуться, нажмите ENTER или введите любое значение")
        input()
        self.base_print()
