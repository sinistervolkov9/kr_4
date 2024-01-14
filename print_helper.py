from vacancy import Vacancy


class PrintHelper:
    def __init__(self):
        self.num = 1

    def to_output(self, data):
        for i in data:
            vac = Vacancy(i["name"], i["salary"], i["link"],  i["region"], i["company"])
            print(f"{self.num}. {vac}")
            self.num += 1
