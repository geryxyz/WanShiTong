import sys
from src.wst.web.webserver import WebServer


try:
    web_server = WebServer()
    # web_server.start()
    web_server.run()
except (KeyboardInterrupt, SystemExit):
    web_server.stop_tornado()
    print('bye')
    sys.exit(0)
