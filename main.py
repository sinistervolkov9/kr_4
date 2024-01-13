from conversion import HHConversion, SJConversion
from interaction import Interaction
from settings import DATA_PATH
from api import HHAPI, SuperjobAPI
from record import Record


class Main:
    def __init__(self):
        self.new_search()

        self.hh_search = True
        self.sj_search = True
        self.resource_list = []

    def new_search(self):
        self.interaction = Interaction()
        self.request_hh = HHAPI()
        self.request_sj = SuperjobAPI()
        self.record_hh = Record(DATA_PATH)
        self.record_sj = Record(DATA_PATH)
        self.conversion_hh = HHConversion()
        self.conversion_sj = SJConversion()

    def run(self):
        keyword = self.interaction.interactive()

        if self.interaction.is_hh_search is True:
            items = self.request_hh.get_request(keyword)
            self.conversion_hh.preparing_for_json(items, self.record_hh, self.resource_list)

        if self.interaction.is_sj_search is True:
            items = self.request_sj.get_request(keyword)
            self.conversion_sj.preparing_for_json(items, self.record_sj, self.resource_list)

        for resource in self.resource_list:
            resource.create_json()


if __name__ == '__main__':
    main = Main()
    main.run()
