from ..module_basehandler import ModulebaseHandler

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        if(self.user_data[self.session] is None):
            self.render("index.html", handler=self)
        else:
            self.render("logged_in_index.html", handler=self)
