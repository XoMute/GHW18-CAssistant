import tornado.ioloop
import tornado.web

import api
import os
os.chdir("Server")
port = os.getenv("PORT",1)


us = api.User("XoMute")

class BaseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("say something")

    def set_default_headers(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
        print(self.request.body)
        print(self.request)


class DialogueChanged(BaseHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        #us.dialogue_changed(self.request.body.decode())
        print(self.request.body)
        self.write("You posted")

class DataHandler(BaseHandler):
    def get(self):
        self.write("Jopa")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/dialogue",DialogueChanged),
        (r"/data",DataHandler)

    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
