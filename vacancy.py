class Vacancy:
    """
    Класса для корректного вывода с данными о вакансии
    """
    def __init__(self, name, salary, link, region, company):
        self.name = name
        self.salary = salary
        self.link = link
        self.region = region
        self.company = company

    def to_json(self):
        """
        Подготовка данных вакансии к json-формату
        :return: dict
        """
        return {"name": self.name, "salary": self.salary, "link": self.link, "region": self.region,
                "company": self.company}

    def __str__(self):
        return f"{self.name};  зарплата: от {self.salary}; ссылка: {self.link}; город: {self.region}; компания: {self.company}"

    def salary_comparison(self, other):
        """
        Сравнение вакансий по зарплате
        :return:
        """
        pass
