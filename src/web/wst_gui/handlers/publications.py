from ..module_basehandler import ModulebaseHandler
from tornado import template
from var_dump import var_dump

from ....utils.beyond import *


class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        ret = self.prepare_site()
        if ret != 100:
            self.render("publications.html", handler=self)

    def prepare_site(self):
        action = self.get_argument("action", None)
        uri = self.request.uri
        self.form_data = []
        split = uri.split('/')
        self.entry = self.get_argument("entry_type", "Article")
        self.switcher = {'Article': Article, 'Book': Book, 'Thesis': Thesis, 'Booklet': Booklet}
        # TODO: If new entry has been made, you have to add to switcher
        self.property_list = self.get_properties(self.switcher[self.entry])
        if not (self.get_secure_cookie("conditions")):
            self.set_secure_cookie("conditions", "0")
            self.number = 0
        else:
            self.number = int(self.get_secure_cookie("conditions"))

        if ("refresh" in uri):
            self.render("elements/browsebar.html", handler=self)
            return 100
        if ("add" in uri):
            self.add_searching_field()
            return 100
        if ("remove" in uri):
            self.remove_searching_field()
            return 100

    def add_searching_field(self):
        """
        It adds one more conditional searching field to the browsebar
        :return:
        """
        self.number = self.number + 1
        self.set_secure_cookie("conditions", str(self.number))
        self.render("elements/browsebar.html", handler=self)
        return

    def remove_searching_field(self):
        if (self.number > 0):
            self.number = self.number - 1
            self.set_secure_cookie("conditions", str(self.number))
        self.render("elements/browsebar.html", handler=self)
        return

    def post(self, *args, **kwargs):
        get_searching_data = []
        self.form_data = []
        entry = self.get_argument("entry_type", "Article")  # book, article etc
        self.number = int(self.get_secure_cookie("conditions"))
        filters = []
        logics = []
        self.entry = Processor.str2entry(entry)  # it will be the processor
        p = Processor(self.entry)
        for i in range(0, self.number):
            condition = self.get_argument("condition_" + str(i), "Contains")
            field = self.get_argument("field_" + str(i), "title")
            value = self.get_argument("value_" + str(i), "")
            if (self.number > i + 1):
                logic = self.get_argument("logical_" + str(i), "OR")
                logics.append(Processor.str2logic(logic))
                self.form_data.append({"condition": condition, "field": field, "value": value, "logic": logic})
            try:
                # filters.append(self.str2filter(condition, field, value))
                filters.append(Processor.str2filter(self.entry, condition, field, value))
            except ValueError as e:
                self.get_warn("danger", str(e))
                self.prepare_site()
                self.render("publications.html", handler=self)
                return
            except UnknownCondition as e:
                self.get_warn("danger", str(e))
                self.prepare_site()
                self.render("publications.html", handler=self)
                return

        try:
            p.filter(filters)
        except ZeroResultException:
            self.get_warn("info", "There were 0 results! Try with other conditions...")
            self.prepare_site()
            self.render("publications.html", handler=self)
            return
        except TypeError:
            self.get_warn("danger", "There were type mismatch! Try again...")
            self.prepare_site()
            self.render("publications.html", handler=self)
            return

        # if 0 results were we dont have to continue with logic...
        p.logic(logics)
        order_by = self.get_argument("order_by", "index")
        order_type = self.get_argument("order", "ascending")
        p.order(order_type, order_by)
        self.result = p.get_result()
        # var_dump(self.result)
        if (not hasattr(self, "result")):
            self.get_warn("danger", "Fill every field!")
            self.prepare_site()
            self.render("publications.html", handler=self)
            return
        self.get_warn("secondary", "There were " + str(len(self.result)) + " results!")
        self.render("results.html", handler=self)

    # def str2entry(self, string):
    #     """
    #     It converts the string which comes from frontend to Processor
    #     :param string:
    #     :return:
    #     """
    #     if(string == "Article"):
    #         self.entry = Article
    #         return Processor(Article)
    #     if(string == "Book"):
    #         self.entry = Book
    #         return Processor(Book)
    # TODO: You have to continue this line

    # def str2logic(self, logic):
    #     if(logic == "OR"):
    #         return Or()
    #     if(logic == "AND"):
    #         return And()
    #     if(logic == "XOR"):
    #         return Xor()
    #     raise UnknownLogic

    # def str2filter(self, condition, field, value):
    #     """
    #     It converts the frontend's string to filter object
    #     :param condition: eg. Equals, Contains etc.
    #     :param field: title, author etc.
    #     :param value: Mandurah, Biden etc.
    #     :return:
    #     """
    #     if condition == "Contains":
    #         return Contains(self.entry.__fields__[field], value)
    #
    #     if condition == "Matches":
    #         return Matches(self.entry.__fields__[field], value)
    #
    #     if condition == "NotContains":
    #         return NotContains(self.entry.__fields__[field], value)
    #
    #     if condition == "NotMatches":
    #         return NotMatches(self.entry.__fields__[field], value)
    #
    #     if condition == "NotEquals":
    #         return NotEquals(self.entry.__fields__[field], value)
    #
    #     if condition == "Equals_or_less":
    #         return Equals_or_less(self.entry.__fields__[field], value)
    #
    #     if condition == "Equals_or_more":
    #         return Equals_or_more(self.entry.__fields__[field], value)
    #
    #     if condition == "Less_than":
    #         return Less_than(self.entry.__fields__[field], value)
    #
    #     if condition == "More_than":
    #         return More_than(self.entry.__fields__[field], value)
    #
    #     if condition == "Equals":
    #         return Equals(self.entry.__fields__[field], value)
    #
    #     raise UnknownCondition(condition + "unknown condition!")
