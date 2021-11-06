import os
from var_dump import var_dump
from tornado import web

class StaticFileHandler(web.StaticFileHandler):

    def write_error(self, status_code, **kwargs):
        self.write("404 page not found") #that calls when static page not found

    def initialize(self, path, default_filename=None):
        self.root = path
