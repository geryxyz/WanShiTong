import tornado.web
import datetime


class ModulebaseHandler(tornado.web.RequestHandler):
    def initialize(self, owner):
        super().initialize()
        self.version = owner.version
        self.authors = owner.authors
        self.release_date = owner.release_date

    def prepare(self):
        pass

    def on_finish(self):
        pass

    def write_error(self, status_code, **kwargs):
        self.render("404.html", error_code=str(status_code))