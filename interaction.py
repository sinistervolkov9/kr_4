class Interaction:
    is_hh_search = True
    is_sj_search = True

    def interactive_start(self):
        print("Привет!\nВведите ключевое слово:")
        keyword = str(input()).title().strip()
        return keyword

    def interactive_resource_search(self):
        print(
            "\nНа каком ресурсе искать? Введите цифру: \n1. HeadHunter\n2. SuperJob\nЕсли это не важно, то просто нажмите ENTER или введите любое значение")
        user_input = str(input()).title().strip()
        print("\nВот что мне удалось найт:")
        return user_input

    def interactive_run(self):
        print(f"ENTER - перейти к следующей\nb - вернуться на предыдущую")
        print(f"\ndf - сравнить вакансии между собой")
        print(f"dl - удалить вакансии, если они вас не интересуют")
        print(f"top - получить топ вакансий по зарплате")
        print(f"e - выйти\n")

        user_input = str(input()).strip()

        return user_input
