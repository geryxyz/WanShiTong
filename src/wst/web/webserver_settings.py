# -*- coding: utf-8 -*-

import os.path

from tornado.options import define, options
# from .gui.handlers import default

class setup_config():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        webserver_ip_port = 80
        print(webserver_ip_port)
        # port = 8080
        #config file will load here
        define("http_port", default=webserver_ip_port, help="run on the given port", type=int)
        # define("https_port", default=443, help="run on the given port", type=int)


# def setup_config(owner):
#     webserver_ip_port = owner.config.get_with_default('webserver','ip_port')
#     # print(webserver_ip_port)
#     # port = 8080
#     define("port", default=webserver_ip_port, help="run on the given port", type=int)
#     define("config", default=None, help="tornado config file")
#     define("debug", default=False, help="debug mode")

#http://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings
settings = {}
from .gui.handlers import static_file_handler
settings["debug"] = True
# settings["debug"] = options.debug()
settings["autoreload"] = True
settings["cookie_secret"] = "Hkj348+%!lkfad22DaorofoJOfeoajf83ij2ZEEZZ_wst_ZZPP"


settings["template_path"] = os.path.join(os.path.dirname(__file__), "gui/templates")


settings["xsrf_cookies"] = False
# settings["xsrf_cookies"] = True
