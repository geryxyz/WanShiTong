from ..module_basehandler import ModulebaseHandler

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        self.content_template = 'content/folders.html'
        self.render("my_folders.html", handler=self)
        if(self.userid is None):
            self.redirect("/index")


    def get_folders(self):
        sqlc = '''SELECT * FROM folders WHERE userid = ?'''
        result = self.Database.query(sqlc, (self.userid,))

