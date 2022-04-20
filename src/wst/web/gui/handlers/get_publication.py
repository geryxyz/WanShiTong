from ..module_basehandler import ModulebaseHandler
from src.wst.utils import *


#/get_publication/Article/199
class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        type = self.get_argument("type", None)
        index = self.get_argument("citekey", None)
        if index is None or type is None:
            #todo exception raising
            raise NotImplementedError()
        type = type.lower()
        entry: Article = Processor.str2entry(type)
        filter = Processor.str2filter(entry, "match_with", "citekey", index)
        filters = []
        filters.append(filter)
        p = Processor(entry)
        p.filter(filters)
        r = p.get_result()
        self.entry = r[0]
        self.fields = entry.getGuiFields(visible_on_gui=True, isTitle=True)
        self.fields_for_backend = entry.getGuiFields(visible_on_gui=True, isTitle=False)
        self.render("publication.html")



