from ..module_basehandler import ModulebaseHandler

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        self.render("login.html", handler=self)

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        rememberme = self.get_argument("rememberme", None)
        print(username, password, rememberme)
        self.render("login.html", handler=self)



