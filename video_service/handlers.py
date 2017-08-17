# coding:utf-8
import re
import tornado.web


class IndexHandler(tornado.web.RequestHandler):

    def get_meta(self, console_info):
        pass

    def is_available(self):
        pass

    def post(self):
        url = self.get_argument('url', "")
        # url = "http://www.iqiyi.com/w_19rvln5aep.html#vfrm=3-17-5-1"
        command = 'you-get -u "%s"' % url
        reply = self.command_2(command)
        video_meta = dict()
        video_meta["page_url"] = url
        self.write("")

    def get(self):
        title = "视频解析测试页面"
        status = ""
        video_meta = dict()
        self.render("index.html",
                    status="请输入页面URL进行解析操作",
                    title=title,
                    video_meta=video_meta)
