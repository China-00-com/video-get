import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import urllib
import json
import datetime
import time

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,
                                          "http://search.twitter.com/search.json?" + \
                                          urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                                                     "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                       time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (query, tweets_per_second))
        self.finish()


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('task', 'Hello')
        print(greeting)
        import you_get
        try:
            you_get.main()
        except Exception as e:
            print(e)
        self.write(greeting + ', friendly user!')


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=
    [
        (r"/", IndexHandler),
        (r"/test", TestHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
