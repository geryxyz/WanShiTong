import tornado.web
import datetime
import os.path
import random
import string
import tornado.template
import hashlib
from var_dump import var_dump

from ...utils.entries.logical import *
from ...utils.entries.filter import *
from ...utils.entries.Article import *

from dateutil.relativedelta import relativedelta

class ModulebaseHandler(tornado.web.RequestHandler):
    def initialize(self, owner):
        super().initialize()
        self.version = owner.version
        self.authors = owner.authors
        self.release_date = owner.release_date
        self.loader = owner.Loader
        self.owner = owner

        # self.elements_dir = os.path.join(self.directory, "templates/elements")
        self.session = self.get_cookie("session", default=None)
        self.userid = self.get_secure_cookie("userid", None)
        self.user_data = {}
        if(len(self.user_data) == 0):
            self.user_data = owner.user_data
        self.Database = owner.Database
        if(self.session is None):
            self.add_cookie()
        # print(self.session)
        self.getUserData(self.user_data[self.session])


    def prepare(self):
        pass

    def on_finish(self):
        pass

    def write_error(self, status_code, **kwargs):
        self.render("404.html", error_code=str(status_code))

    def get_random_string(self, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def add_cookie(self):
        cookie = self.get_random_string(12)
        self.set_cookie("session", cookie)
        sql = ''' INSERT INTO sessions (session, user_id, creation_date, expiry_date, last_usage) VALUES (?, ?, ?, ?, ?) '''
        self.user_data[cookie] = None
        self.session = cookie
        self.Database.queryandcommit(sql, (cookie, None, datetime.datetime.now(), datetime.datetime.now() + relativedelta(months=1), None))

    def get_warn(self, type='primary', message=None):
        # https://getbootstrap.com/docs/4.0/components/alerts/
        possible_types = ['primary', "secondary", "success", "danger", "warning", "info", "light", "dark"]
        if(type not in possible_types):
            type = 'primary'
        self.type=type
        self.web_message=message
        return self.loader.load('elements/warnings/warning-template.html').generate(handler=self)
        # self.warm_html = tornado.template.Template(template_string='elements/warnings/warning-template.html')
        # self.warm_html = self.warm_html.generate(handler=self)
        # print(self.warm_html)
        #

    def login_user(self, userid, username):
        sqlc = ''' UPDATE sessions SET user_id = ? WHERE session = ? '''
        self.Database.queryandcommit(sqlc, (userid, self.session))
        sqlc = ''' UPDATE users SET lastlogin = ? WHERE id = ? '''
        self.Database.queryandcommit(sqlc, (datetime.datetime.now(), userid))
        self.user_data[self.session] = userid
        self.set_secure_cookie("userid", str(userid))
        self.getUserData(userid)
        # self.user_data[self.session] = {'username': username}

    def getUserData(self, id):
        if(self.user_data[self.session] is not None):
            sqlc = ''' SELECT * FROM users WHERE id = ? '''
            data = self.Database.query(sqlc, (id,))
            self.userdata = data[0]
            # var_dump(self.userdata)
            return

    def get_properties(self, target: object):
        annotations = target.__dict__['__annotations__']
        # annotations = target.__fields__
        result = []
        for i in annotations:
            result.append(i)
        return result







