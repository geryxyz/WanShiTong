from ..module_basehandler import ModulebaseHandler

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("userid")
        self.redirect("/index")
