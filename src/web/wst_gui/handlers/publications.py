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
        if("pg" in uri):
            if(self.userid in self.user_processor):
                pr: Processor = self.user_processor[self.userid]
                page_number = self.get_argument("pg", str(1))
                pr.page(page_number)
                self.result = pr.get_result()
                self.get_warn("secondary", "There were " + str(pr.full_results) + " results!")
                self.max_page = pr.maximum_pages
                self.current_page = pr.current_page
                self.render("results.html", handler=self)
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
        p.paging_init(15, 1)
        self.max_page = p.maximum_pages
        self.result = p.get_result()
        self.current_page = 1
        # var_dump(self.result)
        if (not hasattr(self, "result")):
            self.get_warn("danger", "Fill every field!")
            self.prepare_site()
            self.render("publications.html", handler=self)
            return
        self.get_warn("secondary", "There were " + str(p.full_results) + " results!")
        self.user_processor[self.userid] = p
        self.render("results.html", handler=self)



