# Создать функцию для взаимодействия с пользователем.
# Функция должна взаимодействовать с пользователем через консоль.
# Самостоятельно придумать сценарии и возможности взаимодействия с пользователем.
# Например, позволять пользователю указывать, с каких платформ он хочет получить вакансии,
# ввести поисковый запрос, получить топ-N вакансий по зарплате,
# получить вакансии в отсортированном виде, получить вакансии,
# в описании которых есть определенные ключевые слова, например postgres, и т. п.

class Interaction:
    is_hh_search = True  # (вспомогательная для проги)
    is_sj_search = True  # (вспомогательная для проги)
    # Здесь настройки поведения программы

    def interactive_start(self):
        print("Привет!\nВведите ключевое слово:")
        keyword = str(input()).title().strip()

        # print("Что именно искть? Введите цифру: \n1. Должность\n2. Компания\nЕсли это не важно, то просто нажмите Enter")
        # keyword_search = input()
        # print("\nВведите желаемую зарплату:")
        # salary_search = input()
        # print("\nИскать в каком-то определенном регионе? Если да, то введите город, если нет, то просто нажмите Enter")
        # region_search = input()
        print("\nНа каком ресурсе искать? Введите цифру: \n1. HeadHunter\n2. SuperJob\nЕсли это не важно, то просто нажмите Enter")
        resource_search = str(input()).title().strip()
        if resource_search == "1":
            self.is_sj_search = False
        elif resource_search == "2":
            self.is_hh_search = False

        print("\nВот что мне удалось найт:")

        return keyword

    def interactive_run(self):
        print(f"\nСтраница {1} из {10}\nЧтобы перейти к следующей, нажмите Enter\nЧтобы вернуться на предыдущую, введите b")
        print(f"\nВы можете сравнить вакансии между собой. Для этого введите df (запуск скрипта)")
        print(f"Вы можете удалить вакансию, если она вас не интересует. Для этого введите ее номер. После этого список обновится")
        print(f"Вы можете получить топ вакансий по зарплате. Введите кол-во топа\n")

        user_action = str(input()).title().strip()

        return user_action
