from BaseEntry import BaseEntry
from Article import Article
from book import Book
from conditionss import Filter, Logic
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
            raise NotImplementedError
        # and so on!!
        # we have to put several if-es to check these

    def initArticles(self):
        """
        in this function we init EVERY possible article
        :return:
        """
        with open("test_data.json") as file:
            data = json.load(file)
            self.entries: List[Article] = [Article(**item) for item in data]
        # print(self.intermediate)

    # ... initThesis, initPHD, init...

    def initBook(self):
        """
        We initialize here every book
        :return:
        """
        raise NotImplementedError

    def filter(self, *filters: Filter):
        """
        It filters the intermediate. Generates a few tuples one-by-one filters, which intermediate apply
        :param filters:
        :return:
        """
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
        stack = deque()
        stack.append(self.filtered_entries[0])
        stack.append(self.filtered_entries[1])
        logic_helper = self.filtered_entries
        re_set = self.filtered_entries[0]
        counter = 0
        for i in logic:
            re_set = i.analyze(re_set, stack[counter+1])
            # stack.append(re_set)
            # stack.pop()
            counter = counter + 1
        self.final_entries = re_set

    def order(self, *logic: Logic):
        raise NotImplementedError()

    def pagination(self, *logic: Logic):
        raise NotImplementedError()

    def get_result(self):
        if(len(self.filtered_entries) == 1):
            return self.filtered_entries
        else:
            if(hasattr(self, "final_entries")):
                return self.final_entries
            else:
                raise Exception("Logical condition was not given!")
