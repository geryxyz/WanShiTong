from ..module_basehandler import ModulebaseHandler
from src.wst.utils.intermediate import *

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        self.entry_type = self.get_argument("type", "Article")
        citekey = self.get_argument("citekey", None)
        pub_c = Processor.str2entry(self.entry_type)
        p = Processor(pub_c)
        filter = [Processor.str2filter(pub_c, "Matchwith", "citekey", citekey)]
        p.filter(filter)
        self.publication = p.get_result()[0]
        var_dump(self.publication)
        self.fields = pub_c.getGuiFields(True, True) #stands for the user reading
        self.fieldname = pub_c.getGuiFields(True, False) #stands for the software determine which field to write out
        self.render("edit_publication.html", handler=self)

    def post(self):
        citekey = self.get_argument("citekey", None)
        if(citekey is None):
            self.get_warn("danger", "Error! Try again.")
        self.entry_type = self.get_argument("entry_type", "Article")
        pub_type_c = Processor.str2entry(self.entry_type)
        self.fieldname = pub_type_c.getGuiFields(True, False)
        self.fields = pub_type_c.getGuiFields(True, True)  # stands for the user reading
        p = Processor(pub_type_c)
        filter = [Processor.str2filter(pub_type_c, "Matchwith", "citekey", citekey)]
        p.filter(filter)
        self.publication = p.get_result()[0]
        data = {}
        for i in self.fieldname:
            data[i] = self.get_argument(i, None)
        try:
            Processor.editPublication(pub_type_c, data, citekey)
        except NotImplementedError:
            self.get_warn("primary", "This function coming soon!")
        finally:
            self.render("edit_publication.html", handler=self)
