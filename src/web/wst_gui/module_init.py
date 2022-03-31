from .handlers import index
from .handlers import defaultHandler
from .handlers import login
from .handlers import browse
from .handlers import publications
from .handlers import signup
from .handlers import user
from .handlers.static_file_handler import StaticFileHandler
import datetime
from var_dump import var_dump
# from .handlers import default

import tornado.ioloop, tornado.web
import tornado.locale
from tornado import template
import threading
import sys, os
from ...utils.database import Database

from ... import version

class ModuleInit():

    def __init__(self):

        #todo not found 404 error page
        # self.database = ' példányváltozó '
        from ... import version
        self.version = version.__version__
        self.authors = version.__authors__
        self.release_date = version.__release_date__
        self.directory = os.path.dirname(__file__)
        self.user_data = {} #pair of cookie and userid dict
        self.needed_information = {} #additional informations of the user
        self.Loader = template.Loader(os.path.join(self.directory, "templates"))

        static_path = os.path.join(os.path.dirname(__file__), "static")
        handler_parameters = dict(owner=self)
        self.handlers_table=[
            (r"/", index.Index, handler_parameters),
            (r"/index", index.Index, handler_parameters),
            (r"/login", login.Index, handler_parameters),
            (r"/signup", signup.Index, handler_parameters),
            (r"/publications", publications.Index, handler_parameters),
            (r"/publications/(.*)", publications.Index, handler_parameters),
            (r"/users", user.Index, handler_parameters),
            (r"/static/(.*)", StaticFileHandler, {"path": static_path}),
            (r"/(.*)", defaultHandler.Index, handler_parameters),
        ]
        self.Database = Database("wst-db.sqlite")
        self.load_user_sessions()
        # handler_parameters = dict(owner=self, database=self.database)

    def load_user_sessions(self):
        sqlc = '''
         SELECT session, user_id, username FROM sessions LEFT JOIN users ON sessions.user_id=users.id WHERE expiry_date >= ? 
        '''
        result = self.Database.query(sqlc, (datetime.datetime.now(),))
        # var_dump(result)
        print(len(result))
        for i in result:
            if i["user_id"] is None:
                self.user_data[i['session']] = None
            self.user_data[i['session']] = i['user_id']
            # self.user_data[i['session']] = {'username': i['username']}
        # print(len(self.user_data))

