from ..module_basehandler import ModulebaseHandler
from tornado import template
from var_dump import var_dump

from ....utils.entries.Article import Article
from ....utils.entries.Book import Book
from ....utils.entries.processor import Processor
from ....utils.entries.BaseEntry import BaseEntry
from ....utils.entries.conditionss.Logic import Or, Xor, And
from ....utils.entries.conditionss.Filter import Contains, NotContains, Matches, Equals, Equals_or_more, Equals_or_less, NotEquals, NotMatches, More_than, Less_than


class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        self.prepare_site()

        self.render("publications.html", handler=self)

    def prepare_site(self):
        action = self.get_argument("action", None)
        uri = self.request.uri
        self.form_data = []
        split = uri.split('/')
        self.entry = self.get_argument("entry_type", "Article")
        self.switcher = {'Article': Article, 'Book': Book}
        # TODO: If new entry has been made, you have to add to switcher
        self.property_list = self.get_properties(self.switcher[self.entry])
        if not (self.get_secure_cookie("conditions")):
            self.set_secure_cookie("conditions", "0")
            self.number = 0
        else:
            self.number = int(self.get_secure_cookie("conditions"))

        if ("refresh" in uri):
            self.render("elements/browsebar.html", handler=self)
            return
        if ("add" in uri):
            self.add_searching_field()
            return
        if ("remove" in uri):
            self.remove_searching_field()
            return

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
        p = self.str2entry(entry) #it will be the processor
        for i in range(0, self.number):
            condition = self.get_argument("condition_" + str(i), "Contains")
            field = self.get_argument("field_"+str(i), "title")
            value = self.get_argument("value_"+str(i), "")
            if(self.number > i+1):
                logic = self.get_argument("logical_"+str(i), "OR")
                logics.append(self.str2logic(logic))
                self.form_data.append({"condition": condition, "field": field, "value": value, "logic": logic})
            try:
                filters.append(self.str2filter(condition, field, value))
            except ValueError as e:
                self.get_warn("danger", str(e))
                self.prepare_site()
                self.render("publications.html", handler=self)
                #TODO: what to do if string given where int expected

        var_dump(filters)
        p.filter(filters)
        p.logic(logics)
        self.result = p.get_result()
        var_dump(self.result)
        if(not hasattr(self, "result")):
            self.get_warn("danger", "Fill every field!")
            self.prepare_site()
            self.render("publications.html", handler=self)
            return
        if(len(self.result[0]) == 0):
            self.get_warn("info", "There were 0 results! Try with other conditions...")
            self.prepare_site()
            self.render("publications.html", handler=self)
            return
        self.get_warn("secondary", "There were "+str(len(self.result[0]))+" results!")
        self.render("results.html", handler=self)

    def str2entry(self, string):
        """
        It converts the string which comes from frontend to Processor
        :param string:
        :return:
        """
        if(string == "Article"):
            self.entry = Article
            return Processor(Article)
        if(string == "Book"):
            self.entry = Book
            return Processor(Book)
        #TODO: You have to continue this line

    def str2logic(self, logic):
        if(logic == "OR"):
            return Or()
        if(logic == "AND"):
            return And()
        if(logic == "XOR"):
            return Xor()

    def str2filter(self, condition, field, value):
        """
        It converts the frontend's string to filter object
        :param condition: eg. Equals, Contains etc.
        :param field: title, author etc.
        :param value: Mandurah, Biden etc.
        :return:
        """
        if(condition == "Contains"):
            if(len(value) == 0):
                raise ValueError("Empty texts can't be used!")
            return Contains(self.entry.__fields__[field], value)

        if(condition == "Matches"):
            if(len(value) == 0):
                raise ValueError("Empty texts can't be used!")
            return Matches(self.entry.__fields__[field], value)

        if(condition == "NotContains"):
            if(len(value) == 0):
                raise ValueError("Empty texts can't be used!")
            return NotContains(self.entry.__fields__[field], value)

        if(condition == "NotMatches"):
            if(len(value) == 0):
                raise ValueError("Empty texts can't be used!")
            return NotMatches(self.entry.__fields__[field], value)

        if(condition == "NotEquals"):
            if(not isinstance(value, int)):
                raise ValueError("NotEquals condition value must be a number!")
            return NotEquals(self.entry.__fields__[field], int(value))

        if(condition == "Equals_or_less"):
            if(not isinstance(value, int)):
                raise ValueError("Equals or less condition value must be a number!")
            return Equals_or_less(self.entry.__fields__[field], int(value))

        if(condition == "Equals_or_more"):
            if(not isinstance(value, int)):
                raise ValueError("Equals or more condition must be a number!")
            return Equals_or_more(self.entry.__fields__[field], int(value))

        if(condition == "Less_than"):
            if not isinstance(value, int):
                raise ValueError("Less than condition value must be a number!")
            return Less_than(self.entry.__fields__[field], int(value))

        if(condition == "More_than"):
            if(not isinstance(value, int)):
                raise ValueError("More than condition value must be a number!")
            return More_than(self.entry.__fields__[field], int(value))

        if(condition == "Equals"):
            if(not isinstance(value, int)):
                raise ValueError("Equals condition value must be a number!")
            return Equals(self.entry.__fields__[field], int(value))






