from .handlers import index
from .handlers import defaultHandler
from .handlers import login
from .handlers import browse
from .handlers import publications
from .handlers.static_file_handler import StaticFileHandler
# from .handlers import default

import tornado.ioloop, tornado.web
import tornado.locale
import threading
import sys, os

from ... import version

class ModuleInit():

    def __init__(self):

        #todo not found 404 error page
        # self.database = ' példányváltozó '
        from ... import version
        self.version = version.__version__
        self.authors = version.__authors__
        self.release_date = version.__release_date__
        self.user_data = {}

        static_path = os.path.join(os.path.dirname(__file__), "static")
        handler_parameters = dict(owner=self)
        self.handlers_table=[
            (r"/", index.Index, handler_parameters),
            (r"/login", login.Index, handler_parameters),
            (r"/publications", publications.Index, handler_parameters),
            (r"/static/(.*)", StaticFileHandler, {"path": static_path}),
            (r"/(.*)", defaultHandler.Index, handler_parameters),
        ]

        # handler_parameters = dict(owner=self, database=self.database)
