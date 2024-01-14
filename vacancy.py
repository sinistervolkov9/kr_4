# Создать класс для работы с вакансиями.
# Обрабатывает данные
class Vacancy:
    def __init__(self, name, salary, link, region, company):
        # Класс должен валидировать данные, которыми инициализируются его атрибуты.
        # if not isinstance(name, str): # or not isinstance(salary, int):
        #     raise TypeError("Неверный тип данных")
        # if not name or salary < 0:
        #     raise ValueError("Неверное значение данных")

        self.name = name
        self.salary = salary
        self.link = link
        self.region = region
        self.company = company

    def to_json(self):
        return {"name": self.name, "salary": self.salary, "link": self.link, "region": self.region,
                "company": self.company}

    def __str__(self): # А зачем это?
        return f"{self.name};  зарплата: от {self.salary}; ссылка: {self.link}; город: {self.region}; компания: {self.company}"


    # Класс должен поддерживать методы сравнения вакансий между собой по зарплате
    def salary_comparison(self):
        """
        Сравнение вакансий по зарплате
        :return:
        """
        pass


# class HHVacancy(Vacancy):
#     def __init__(self, name, salary, link, description):
#         super().__init__(name, salary, link, description)
#         pass
#
#     def __str__(self):
#         return f"HH:{self.name}, зарплата: {self.salary} руб.мес"
#
#
# class SJVacancy(Vacancy):
#     def __init__(self, name, salary, link, description):
#         super().__init__(name, salary, link, description)
#         pass
#
#     def __str__(self):
#         return f""
