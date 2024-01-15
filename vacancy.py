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

    def __str__(self):
        return f"{self.name};  зарплата: от {self.salary}; ссылка: {self.link}; город: {self.region}; компания: {self.company}"

    def to_comparison(self):
       pass

    def salary_comparison(self, other):
        """
        Сравнение вакансий по зарплате
        :return:
        """
        return self.salary > other.salary
