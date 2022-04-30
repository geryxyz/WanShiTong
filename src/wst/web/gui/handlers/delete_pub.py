from ..module_basehandler import ModulebaseHandler
from src.wst.utils.intermediate import *

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        confirmed = self.get_argument("confirm", None)
        self.entry_type = self.get_argument("entry_type", None)
        self.citekey = self.get_argument("citekey", None)
        if(confirmed is None):
            self.render("delete_pub.html")
        elif(confirmed == "true"):
            try:
                Processor.deletePublication(Processor.str2entry(self.entry_type), self.citekey)
            except NotImplementedError:
                self.get_warn("primary", "This function is coming soon!")
            finally:
                self.render("delete_pub.html")
