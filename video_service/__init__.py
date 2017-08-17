# coding:utf-8
import os
import tornado.web
from video_service.routers import service_routers
from video_service.settings import SETTINGS


class Application(tornado.web.Application):
    def __init__(self):
        handlers = service_routers
        settings = SETTINGS
        super(Application, self).__init__(handlers, **settings)
        # self.glob_var =
        self.other_init()

    def other_init(self):
        pass


app = Application()
