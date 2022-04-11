from pydantic.typing import Union, List

from collections import deque
from .conditions import *
from .entries import *
from .exceptions import *

import json
from typing import List
from pydantic.fields import ModelField, Union


class Processor():
    def __init__(self, source: BaseEntry):
        """
        We wait for each entry type.
        :param source:
        """
        self.filtered_entries = []
        self.source = source

        if source == Article:  # this is how we can check our input
            self.initArticles()
        if source == Book:
            raise NotImplementedError()
        self.used_filters = []
        self.used_logics = []
        self.used_order = None
        self.used_pagination = None
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
            # self.beyond = [Article()]
        # print(self.beyond)

    # ... initThesis, initPHD, init...

    def initBook(self):
        """
        We initialize here every book
        :return:
        """
        raise NotImplementedError

    def filter(self, *filters: Filter):
        """
        It filters the beyond. Generates a few tuples one-by-one filters, which beyond apply
        :param filters:
        :return:
        """
        filters = filters[0]
        one_by_one_filter = []
        self.used_filters = filters
        for filter in filters:
            one_by_one_filter = []
            for entry in self.entries:
                try:
                    if (filter.is_pass(entry)):
                        one_by_one_filter.append(entry)
                except TypeError:
                    raise TypeError()
                    # print(one_by_one_filter)
            self.filtered_entries.append(one_by_one_filter)
        # self.final_entries = self.filtered_entries
        for elem in self.filtered_entries:
            if len(elem) > 0:
                return
        raise ZeroResultException("There were 0 results! Try with other conditions...")

    def logic(self, *logic: Logic):
        logic = logic[0]
        self.used_logics = logic
        if len(logic) == 0:
            if len(self.filtered_entries) > 1:
                raise LogicalWasNotGiven("Logical condition was not given!")
            self.final_entries = self.filtered_entries[0]
            self.original_results = self.final_entries
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
        self.original_results = self.final_entries

    def order(self, order_type: str, field: str):
        self.used_order = Processor.str2order(order_type, field)
        self.final_entries = self.used_order.order(self.final_entries)
        self.original_results = self.final_entries

    def paging_init(self, entry_per_page: int, pgnumber: int):
        self.pagination = Paging(entry_per_page, self.final_entries)
        self.full_results = len(self.original_results)
        self.maximum_pages = self.pagination.get_pages_number()
        self.final_entries = self.pagination.getpage(1)
        self.current_page = pgnumber

    def page(self, way: str):
        # way: plus-minus
        way = way.lower()
        if way == "next":
            self.final_entries = self.pagination.next_page()
            self.current_page = self.pagination.pgnumber
            return
        elif way == "previous":
            self.final_entries = self.pagination.previous_page()
            self.current_page = self.pagination.pgnumber
            return
        try:
            way = int(way)
        except ValueError:
            raise TooManyPages()  # do job to handle: s does not contain anything convertible to int
        except Exception as ex:
            raise TooManyPages()  # do job to handle: Exception occurred while converting to int

        self.final_entries = self.pagination.getpage(int(way))
        self.current_page=self.pagination.pgnumber
        return



    def get_result(self):
        # if (len(self.filtered_entries) == 1):
        #     return self.filtered_entries
        # else:
        #     if (hasattr(self, "final_entries")):
        #         return self.final_entries
        #     else:
        #         raise Exception("Logical condition was not given!")
        if not hasattr(self, "final_entries"):
            return self.filtered_entries[0]
        return self.final_entries


    @classmethod
    def str2filter(cls, entry, condition: str, field, value):
        """
        It converts the frontend's string to filter object
        :param entry: entry
        :param condition: eg. Equals, Contains etc.
        :param field: title, author etc.
        :param value: Mandurah, Biden etc.
        :return:
        """
        condition=condition.lower()
        if condition == "contains":
            return Contains(entry.__fields__[field], value)

        if condition == "matches":
            return Matches(entry.__fields__[field], value)

        if condition == "notcontains":
            return NotContains(entry.__fields__[field], value)

        if condition == "notmatches":
            return NotMatches(entry.__fields__[field], value)

        if condition == "notequals":
            return NotEquals(entry.__fields__[field], value)

        if condition == "equals_or_less":
            return Equals_or_less(entry.__fields__[field], value)

        if condition == "equals_or_more":
            return Equals_or_more(entry.__fields__[field], value)

        if condition == "less_than":
            return Less_than(entry.__fields__[field], value)

        if condition == "more_than":
            return More_than(entry.__fields__[field], value)

        if condition == "equals":
            return Equals(entry.__fields__[field], value)

        raise UnknownCondition(condition + "unknown condition!")

    @classmethod
    def str2logic(cls, logic: str):
        logic = logic.lower()
        if logic == "or":
            return Or()
        if logic == "and":
            return And()
        if logic == "xor":
            return Xor()
        raise UnknownLogic()

    @classmethod
    def str2entry(cls, entry: str):
        """
        It converts the string which comes from frontend to Processor
        :param cls:
        :return:
        """
        entry = entry.lower()
        if entry == "article":
            return Article
            # return Processor(Article)
        if entry == "book":
            return Book
            # return Processor(Book)
        raise UnknownEntry()

    @classmethod
    def str2order(cls, order: str, field: str):
        order = order.lower()
        if order == "descending":
            return DescendingOrder(field)
        if order == "ascending":
            return AscendingOrder(field)
        raise UnknownOrder()