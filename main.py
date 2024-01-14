from settings import DATA_PATH, DATA_PATH_HH, DATA_PATH_SJ
from api import HHAPI, SuperjobAPI
from interaction import Interaction
from record import Record
from converter import HHConversion, SJConversion, PrintHelper
from response_handler import ResponseHandler


class Main:
    def __init__(self):
        self.new_search()
        self.hh_vac_list = []
        self.sj_vac_list = []

    def new_search(self):
        self.interaction = Interaction()
        self.request_hh = HHAPI()
        self.request_sj = SuperjobAPI()
        self.record_file = Record(DATA_PATH)
        self.record_hh = Record(DATA_PATH_HH)
        self.record_sj = Record(DATA_PATH_SJ)
        self.hhconversion = HHConversion()
        self.sjconversion = SJConversion()
        #self.printhelper = PrintHelper()
        self.response_handler = ResponseHandler()

    def run(self):
        keyword = self.interaction.interactive_start()
        user_input = self.interaction.interactive_resource_search()

        self.response_handler.resource_search(user_input)
        if self.response_handler.is_hh_search is True:
            vacancies = self.request_hh.get_request(keyword)
            self.record_hh.add_to_json(vacancies)
            data = self.record_hh.get_data()
            self.hh_vac_list = self.hhconversion.for_print(data)
        if self.response_handler.is_sj_search is True:
            vacancies = self.request_sj.get_request(keyword)
            self.record_sj.add_to_json(vacancies)
            data = self.record_sj.get_data()
            self.sj_vac_list = self.sjconversion.for_print(data)
        self.record_file.create_json(self.hh_vac_list, self.sj_vac_list)

        data = self.record_file.get_data()
        self.printhelper = PrintHelper(data)
        self.printhelper.base_print()

        while True:
            a = self.interaction.interactive_run()
            self.printhelper.response_handler(a)


if __name__ == '__main__':
    main = Main()
    main.run()
