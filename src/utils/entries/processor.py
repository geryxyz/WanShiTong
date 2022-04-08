from ..entries.BaseEntry import BaseEntry
from ..entries.Article import Article
from ..entries.Book import Book
from pydantic.typing import Union, List
from conditionss import Filter, Logic, Pagination, Order
from collections import deque


import json
from typing import List


class Processor():
    def __init__(self, source: BaseEntry):
        """
        We wait for each entry type.
        :param source:
        """
        self.source = source

        if source == Article:  # this is how we can check our input
            self.initArticles()
        if source == Book:
            raise NotImplementedError()
        # and so on!!
        # we have to put several if-es to check these

    def initArticles(self):
        """
        in this function we init EVERY possible article
        :return:
        """
        # TODO: You have to init Articles from Bib here
        with open("test_data.json") as file:
            data = json.load(file)
            self.entries: List[Article] = [Article(**item) for item in data]
            # self.entries = [Article()]
        # print(self.entries)

    # ... initThesis, initPHD, init...

    def initBook(self):
        """
        We initialize here every book
        :return:
        """
        raise NotImplementedError

    def filter(self, *filters: Filter):
        """
        It filters the entries. Generates a few tuples one-by-one filters, which entries apply
        :param filters:
        :return:
        """
        filters = filters[0]
        self.filtered_entries = []
        one_by_one_filter = []
        for filter in filters:
            one_by_one_filter = []
            for entry in self.entries:
                if (filter.is_pass(entry)):
                    one_by_one_filter.append(entry)
                    # print(one_by_one_filter)
            self.filtered_entries.append(one_by_one_filter)
        # print(self.filtered_entries)

    def logic(self, *logic: Logic):
        logic = logic[0]
        if(len(logic) == 0):
            self.final_entries = self.filtered_entries[0]
            return
        logic_helper = self.filtered_entries
        re_set = self.filtered_entries[0]
        counter = 0
        for i in logic:
            re_set = i.analyze(re_set, logic_helper[counter + 1])
            # stack.append(re_set)
            # stack.pop()
            counter = counter + 1
        self.final_entries = re_set

    def order(self, *logic: Logic):
        raise NotImplementedError()

    def pagination(self, *logic: Logic):
        raise NotImplementedError()

    def get_result(self):
        if (len(self.filtered_entries) == 1):
            return self.filtered_entries
        else:
            if (hasattr(self, "final_entries")):
                return self.final_entries
            else:
                raise Exception("Logical condition was not given!")
