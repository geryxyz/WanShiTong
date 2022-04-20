from urllib.request import urlopen
from urllib.parse import urlencode
import tornado.httpserver
import tornado.ioloop
import tornado.web

# To obtain key: https://www.google.com/recaptcha/whyrecaptcha
publickey = ' Fill in you  public key'
privatekey = ' Fill in you  private key'


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler)
        ]
        settings = dict(
            template_path="templates",
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', publickey=publickey)

    def post(self):
        url = 'http://www.google.com/recaptcha/api/verify'

        # Verification code
        challenge = self.get_argument('recaptcha_challenge_field')
        # User input
        response = self.get_argument('recaptcha_response_field')

        data = {
            'privatekey': privatekey,
            'remoteip': self.request.remote_ip,
            'challenge': challenge,
            'response': response
        }

        res = urlopen(url, data=urlencode(data).encode())
        # Gets the validation results, which are output directly to the page
        self.write(res.read().decode())


if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(10001)
    tornado.ioloop.IOLoop.instance().start()