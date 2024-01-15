import sys
from settings import DATA_PATH, DATA_PATH_HH, DATA_PATH_SJ, ResourceSearch
from api import HHAPI, SuperjobAPI
from interaction import Interaction
from record import Record
from converter import HHConversion, SJConversion
from print_helper import PrintHelper


class Main:
    def __init__(self):
        self.new_search()
        self.hh_vac_list = []
        self.sj_vac_list = []
        self.running = True

    def new_search(self):
        self.interaction = Interaction()
        self.request_hh = HHAPI()
        self.request_sj = SuperjobAPI()
        self.record_file = Record(DATA_PATH)
        self.record_hh = Record(DATA_PATH_HH)
        self.record_sj = Record(DATA_PATH_SJ)
        self.hhconversion = HHConversion()
        self.sjconversion = SJConversion()
        self.resource_search = ResourceSearch()

    def run(self):
        keyword = self.interaction.interactive_start()
        user_input = self.interaction.interactive_resource_search()

        self.resource_search.resource_search(user_input)
        if self.resource_search.is_hh_search is True:
            vacancies = self.request_hh.get_request(keyword)
            self.record_hh.add_to_json(vacancies)
            data = self.record_hh.get_data()
            self.hh_vac_list = self.hhconversion.for_print(data)
        if self.resource_search.is_sj_search is True:
            vacancies = self.request_sj.get_request(keyword)
            self.record_sj.add_to_json(vacancies)
            data = self.record_sj.get_data()
            self.sj_vac_list = self.sjconversion.for_print(data)
        self.record_file.create_json(self.hh_vac_list, self.sj_vac_list)

        data = self.record_file.get_data()
        self.printhelper = PrintHelper(data)
        self.printhelper.base_print()

        while self.running:
            user_input = self.interaction.interactive_run()

            if user_input == "":
                self.printhelper.next_page()
            elif user_input == "b":
                self.printhelper.previous_page()
            elif user_input == "df":
                self.printhelper.comparison_vac()
            elif user_input == "dl":
                user_input = self.printhelper.remove_vac()
                self.record_file.remove_data(user_input)
                data = self.record_file.get_data()
                self.printhelper = PrintHelper(data)
                self.printhelper.base_print()
            elif user_input == "top":
                self.printhelper.top_vac()
            elif user_input == "e":
                self.running = False
                sys.exit()
            else:
                self.printhelper.no_comand()


if __name__ == '__main__':
    main = Main()
    main.run()
