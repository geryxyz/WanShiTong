import math
from ..exceptions import *
from pydantic.fields import List

class Paging():
    def __init__(self, entry_per_page: int, collection: List):
        self.entry_per_page = entry_per_page
        self.collection = collection

    def getpage(self, pgnumber):
        self.pgnumber = pgnumber
        if pgnumber > self.get_pages_number() or (pgnumber < 1):
            raise TooManyPages("Invalid page number!")
        return [self.collection[i:i + self.entry_per_page] for i in range(0, len(self.collection), self.entry_per_page)][self.pgnumber]
        # return [self.collection[i:i + self.entry_per_page] for i in range(0, len(self.collection), self.entry_per_page)][self.pgnumber]

    def get_pages_number(self):
        """
        Returns how many page there will be
        :return:
        """
        return math.ceil(len(self.collection) / self.entry_per_page)

    def next_page(self):
        self.pgnumber=self.pgnumber+1
        return self.getpage(self.pgnumber)

    def previous_page(self):
        self.pgnumber=self.pgnumber-1
        return self.getpage(self.pgnumber)

