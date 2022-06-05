from ..module_basehandler import ModulebaseHandler

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        self.render("404.html", handler=self)
