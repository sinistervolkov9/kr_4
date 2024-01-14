import sys


class ResponseHandler:
    is_hh_search = True
    is_sj_search = True
    input_list = ["", "b", "df", "dl", "top", "e"]

    def check_input(self, user_input):
        if user_input in self.input_list:
            print("Такой команды нет\n")

    def resource_search(self, user_input):
        if user_input == "1":
            self.is_sj_search = False
        elif user_input == "2":
            self.is_hh_search = False










    def next_page(self, user_input):
        if user_input == "":
            return 1

    def previous_page(self, user_input):
        if user_input == "b":
            return -1

    def comparison(self, user_input):
        choice_list = []
        if user_input == "df":
            user_choice = input("Введите номера вакансий, которые хотите сравнить").split()
            for i in user_choice:
                if isinstance(i, int) or i.isdigit():
                    number = int(i)
                    choice_list.append(number)
                else:
                    print(f"{i} - это не число")
            return choice_list

    def remove(self, user_input):
        choice_list = []
        if user_input == "dl":
            user_choice = input("Введите номера вакансий, которые хотите удалить").split()
            for i in user_choice:
                if isinstance(i, int) or i.isdigit():
                    number = int(i)
                    choice_list.append(number)
                else:
                    print(f"{i} - это не число")
            return choice_list

    def top(self, user_input):
        if user_input == "top":
            pass

    def exit(self, user_input):
        if user_input == "e":
            sys.exit()
