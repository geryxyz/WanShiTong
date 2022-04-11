from ..module_basehandler import ModulebaseHandler
import hashlib
import datetime

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        # self.web_message = self.get_warn('primary', 'Teszt')
        self.username = None
        self.email = None
        self.password = None
        self.password_again = None
        self.checkbox = None
        self.render("signup.html", handler=self)

    def post(self):
        #todo lehetne több adatot is bekérni majd
        self.username = self.get_argument("username", None)
        self.email = self.get_argument("email", None)
        self.password = self.get_argument("password", None)
        self.password_again = self.get_argument("password_again", None)
        self.checkbox = self.get_argument("checkbox", None)
        print(self.username)
        if(self.password != self.password_again):
            self.get_warn("danger", "The two passwords do not match!")
            self.render("signup.html", handler=self)
            return
        elif(len(self.password) < 8):
            self.get_warn("danger", "The password must be at minimum 8 characters long!")
            self.render("signup.html", handler=self)
            return
        sqlc = """SELECT id FROM users WHERE username = ? OR email = ?"""
        result = self.Database.query(sqlc, (self.username,self.email))
        if(len(result) > 0):
            self.get_warn("danger", "The user or email already exists!")
            self.render("signup.html", handler=self)
            return
        if(self.checkbox is None):
            self.get_warn("danger", "You have to agree with the Terms & Conditions!")
            self.render("signup.html", handler=self)
            return
        password_hashed = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        sqlc = '''INSERT INTO users (username, password, regdate) VALUES (?, ?, ?)'''
        self.Database.queryandcommit(sqlc, (self.username, password_hashed, datetime.datetime.now()))
        self.get_warn("success", "You have succesfully registered! Now log in!")
        self.render("login.html", handler=self)



