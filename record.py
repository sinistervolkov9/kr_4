import json


class Record:
    def __init__(self, data):
        self.data = data
        self.vacancy_list = []

    def create_json(self, list_1, list_2):
        self.vacancy_list.extend(list_1)
        self.vacancy_list.extend(list_2)

        with open(self.data, "w", encoding="utf-8") as file:
            json.dump(self.vacancy_list, file, ensure_ascii=False)

    def add_to_json(self, vacancies):
        """
        Добавление вакансий (и данных о них) в файл
        Принимает список, и записывает его в json-файл
        :return:
        """
        with open(self.data, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def get_data(self):
        """
        Получение данных из файла по указанным критериям
        :return:
        """
        with open(self.data, 'r', encoding="utf-8") as file:
            file_data = json.load(file)
            return file_data

    def remove_data(self, rem_list: list):
        """
        Удаления информации о вакансиях (и об их данных) из файла
        (Очистка по номеру строки, введенной пользователем)
        :return:
        """
        num = 0
        removed_list = []

        with open(self.data, 'r', encoding="utf-8") as file:
            file_data = json.load(file)
            for i in rem_list:
                if i > 0 and i <= len(file_data) and i not in removed_list:
                    file_data.pop(i - 1 - num)
                    removed_list.append(i)
                    num += 1

        with open(self.data, "w", encoding="utf-8") as file:
            json.dump(file_data, file, ensure_ascii=False)
