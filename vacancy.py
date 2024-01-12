# Создать класс для работы с вакансиями.
# Это данные на запись в json?
class Vacancy:
    # В этом классе самостоятельно определить атрибуты, такие как:
    name: str = ""  # название вакансии
    salary: int = 123  # зарплата
    link: str = "123"  # ссылка на вакансию
    description: str = "123"  # краткое описание
    # region: str = "123"  # регион
    # experience: bool = False  # требуется ли опыт работы

    def __init__(self, name, salary, link, description):
        # Класс должен валидировать данные, которыми инициализируются его атрибуты.
        if not isinstance(name, str) or not isinstance(salary, int):
            raise TypeError("Неверный тип данных")
        if not name or salary < 0:
            raise ValueError("Неверное значение данных")

        self.name = name
        self.salary = salary
        self.link = link
        self.description = description

    def __repr__(self):
        return f"vacancy(name = '{self.name}', link = '{self.link}', description = '{self.description}', salary = {self.salary}"

    # Класс должен поддерживать методы сравнения вакансий между собой по зарплате
    def salary_comparison(self):
        """
        Сравнение вакансий по зарплате
        :return:
        """
        pass


class HHVacancy(Vacancy):
    def __init__(self, name, salary, link, description):
        super().__init__(name, salary, link, description)
        pass

    def __str__(self):
        return f"HH:{self.name}, зарплата: {self.salary} руб.мес"


class SJVacancy(Vacancy):
    def __init__(self, name, salary, link, description):
        super().__init__(name, salary, link, description)
        pass

    def __str__(self):
        return f""
