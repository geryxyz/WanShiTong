from ..module_basehandler import ModulebaseHandler
from ....utils.beyond import *
from var_dump import var_dump

#/get_publication/Article/199
class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        type = self.get_argument("type", None)
        index = self.get_argument("index", None)
        if index is None or type is None:
            #todo exception raising
            raise NotImplementedError()
        type = type.lower()
        entry: BaseEntry = Processor.str2entry(type)
        filter = Processor.str2filter(entry, "equals", "index", index)
        filters = []
        filters.append(filter)
        p = Processor(entry)
        p.filter(filters)
        r = p.get_result()
        self.entry = r[0]
        self.fields = entry.get_field_names()
        self.render("publication.html")



