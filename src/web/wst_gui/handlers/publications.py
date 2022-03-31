from ..module_basehandler import ModulebaseHandler
from tornado import template

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        action = self.get_argument("action", None)
        uri = self.request.uri
        split = uri.split('/')
        if not (self.get_secure_cookie("conditions")):
            self.set_secure_cookie("conditions", "0")
            self.number = 0
        else:
            self.number = int(self.get_secure_cookie("conditions"))

        if("add" in uri):
            self.add_searching_field()
            return
        if("remove" in uri):
            self.remove_searching_field()
            return

        self.render("publications.html", handler=self)

    def add_searching_field(self):
        self.number = self.number + 1
        self.set_secure_cookie("conditions", str(self.number))
        self.render("elements/browsebar.html", handler=self)
        return

    def remove_searching_field(self):
        if(self.number > 0):
            self.number = self.number - 1
            self.set_secure_cookie("conditions", str(self.number))
        self.render("elements/browsebar.html", handler=self)
        return

    def post(self, *args, **kwargs):
        get_searching_data = []
        self.number = int(self.get_secure_cookie("conditions"))
        for i in range(0, self.number):
            #és itt kéne ezt a fura objektumot felépíteni
            pass