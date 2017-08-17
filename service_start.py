# coding:utf-8

import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options
from video_service import app

if __name__ == "__main__":
    define("port", default=8000, help="run on the given port", type=int)
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
