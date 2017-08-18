# coding:utf-8

from video_service.handlers import *
from settings import SETTINGS

service_routers = [
    (r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=SETTINGS['static_path'])),
    (r'/', IndexHandler),
    (r'/test', m3u8Handler),
    (r'/jsparser', JsVideoParserHandler),
]
