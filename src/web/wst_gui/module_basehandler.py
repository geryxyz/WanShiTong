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
        # raise Exception('Error!')
        # self.set_status(301)


    def on_finish(self):
        pass

    def write_error(self, status_code, **kwargs):
        self.write("Error! Error code: "+str(status_code))