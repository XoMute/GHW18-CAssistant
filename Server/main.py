import tornado.ioloop
import tornado.web

import api
import os
os.chdir("Server")
port = os.getenv("PORT",1)


us = api.User("XoMute")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class DialogueChanged(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        print(sels.request.body)
        self.write("You posted")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/dialogue",DialogueChanged)

    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
