import pydantic.error_wrappers

from ..module_basehandler import ModulebaseHandler
from ....utils.beyond import *

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        global publication
        self.type = self.get_argument("entry_type", None)
        if(self.type is not None):
            try:
                publication = Processor.str2entry(self.type)
            except UnknownEntry():
                self.get_warn("danger", "Invalid entry type has been given!")
                self.render("add_publication.html")
           # p = Processor(publication)
            self.fields = publication.get_field_names()
            self.render("add_pub_form.html", handler=self)
            return
        self.render("add_publication.html")


    def post(self):
        type = self.get_argument("entrytype", None)
        entry = Processor.str2entry(type)
        dict = {}
        for i in entry.get_field_names():
            dict[i] = self.get_argument(i, None)
            if(dict[i] is None):
                self.get_warn("danger", "You have to fill every field!")
                self.render("add_publication.html")
                return
        try:
            publication = entry.parse_obj(dict)
        except pydantic.error_wrappers.ValidationError as e:
            self.get_warn("danger", "You have to fill correctly every field!")
            self.render("add_publication.html")
            return
        try:
            Processor.addPublication(entry, publication)
        except NotImplementedError:
            self.get_warn("primary", "This function is coming soon!")
            self.render("add_publication.html")



