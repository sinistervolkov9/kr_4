import json

# Определить абстрактный класс, который обязывает реализовать методы
# для добавления вакансий в файл, получения данных из файла
# по указанным критериям и удаления информации о вакансиях.
# Создать класс для сохранения информации о вакансиях в JSON-файл.

# Работает с файлом
class Record:

    vacancy_list = []

    def __init__(self, data):
        self.data = data

        #self.create_json()

    def create_json(self, list_1, list_2):
        # Создает общий файл для вакансий. А зачем? Чтобы парсить потом из него
        self.vacancy_list.extend(list_1)
        self.vacancy_list.extend(list_2)

        with open(self.data, "w", encoding="utf-8") as file:
            json.dump(self.vacancy_list, file, ensure_ascii=False)

    def add_to_json(self, vacancies):
        """
        Добавление вакансий (и данных о них) в файл
        :return:
        """
        # Принимает список, и записывает его в json-файл
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

    def remove_data(self):
        """
        Удаления информации о вакансиях (и об их данных) из файла
        (Очистка файла)
        :return:
        """
        pass
        # очистка файла полностью
        # очистка по номеру строки, введенной пользователем
