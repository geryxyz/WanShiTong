from ..module_basehandler import ModulebaseHandler
import hashlib

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        self.username = None
        self.password = None
        self.rememberme = None
        self.render("login.html", handler=self)

    def post(self, *args, **kwargs):
        self.username = self.get_argument("username", None)
        self.password = self.get_argument("password", None)
        self.rememberme = self.get_argument("rememberme", None)
        if(self.username is None or len(self.username) == 0):
            self.get_warn("warning", "You have to enter the username!")
            self.render("login.html", handler=self)
            return
        if(self.password is None or len(self.password) == 0):
            self.get_warn("warning", "You have to enter the password!")
            self.render("login.html", handler=self)
            return
        pw = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        sqlc = ''' SELECT id FROM users WHERE username = ? AND password = ?'''
        result = self.Database.query(sqlc, (self.username, pw))
        if(len(result) == 1):
            self.login_user(result[0]['id'], self.username)
        else:
            self.get_warn("danger", "You have entered the wrong password or the user does not exists!")
        self.render("index.html", handler=self)



