# -*- coding: utf-8 -*-

import os.path

from tornado.options import define, options
from src.wst.utils.config_parser import CParser
# from .gui.handlers import default

class setup_config():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = CParser()
        self.setup()

    def setup(self):
        port = self.c.getdata("port")
        webserver_ip_port = port
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
c = CParser()
#http://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings
settings = {}
from .gui.handlers import static_file_handler
settings["debug"] = True
# settings["debug"] = options.debug()
settings["autoreload"] = True
settings["cookie_secret"] = c.getdata("cookie-secret")


settings["template_path"] = os.path.join(os.path.dirname(__file__), "gui/templates")


settings["xsrf_cookies"] = False
    # settings["xsrf_cookies"] = True
