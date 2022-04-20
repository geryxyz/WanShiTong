#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
import tornado.web
from tornado.options import options
from tornado import ioloop
from . import webserver_settings

class WebServer():
    def run(self):
            self.start_tornado()

    def start_tornado(self):
        app = TornadoApplication()
        app.listen(options.http_port)
        http_server = tornado.httpserver.HTTPServer(
            app,
        )
        #todo setup the tornado based options/config where we can set the port
        http_server.listen(1800)
        # http_server.listen(options.http_port)
        tornado.ioloop.IOLoop.current().start()
        return

    def stop_tornado(self):
        tornado.ioloop.IOLoop.instance().stop()

class TornadoApplication(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        tornado.web.Application.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)

        webserver_settings.setup_config()

        handlers = []
        modules = []

        # for dirlist:
        from .gui import module_init
        module = module_init.ModuleInit()
        modules.append(module)
        handlers.extend(module.handlers_table)

        # default_handler
        # from .default_module import module_init
        # module = module_init.ModuleInit()
        # modules.append(module)
        # handlers.extend(module.handlers_table)

        # tornado.options.parse_command_line()
        tornado.web.Application.__init__(self, handlers, **webserver_settings.settings)
        # var_dump(webserver_settings.settings)
        # http://www.tornadoweb.org/en/stable/web.html#application-configuration

if __name__ == "__main__":
    import time

    print ("Your web server started")
    a = WebServer()
    # a.start()
    a.run()

    # threading.Thread(target=start_tornado).start()
    try:
        # myServer.serve_forever()
	# tornado.ioloop.IOLoop.current().start()
        while 1:
           time.sleep(10)
        tornado.ioloop.IOLoop.instance().stop()
    except (KeyboardInterrupt, SystemExit):
        tornado.ioloop.IOLoop.instance().stop()
        pass
        sys.exit(0)
