from ..module_basehandler import ModulebaseHandler
from src.wst.utils import *


#/get_publication/Article/199
class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        self.entry_type = self.get_argument("entry_type", None)
        self.citekey = self.get_argument("citekey", None)
        if self.citekey is None or type is None:
            #todo exception raising
            raise NotImplementedError()
        self.entry_type = self.entry_type.lower()
        entry: Article = Processor.str2entry(self.entry_type)
        filter = Processor.str2filter(entry, "match_with", "citekey", self.citekey)
        self.fieldname = entry.getGuiFields(True, False)
        self.fields = entry.getGuiFields(True, True)  # stands for the user reading
        filters = []
        filters.append(filter)
        p = Processor(entry)
        p.filter(filters)
        r = p.get_result()
        self.publication = r[0]
        self.fields = entry.getGuiFields(visible_on_gui=True, isTitle=True)
        self.fields_for_backend = entry.getGuiFields(visible_on_gui=True, isTitle=False)
        self.render("publication.html")



