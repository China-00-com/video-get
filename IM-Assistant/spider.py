# coding:utf-8

import re
from urllib2 import quote
import requests


class SearchBase(object):

    def search(self, name):
        pass


class XkanbaSearch(SearchBase):
    SEARCH_URL = "http://xkanba.com/index.php?m=vod-search-wd-{name}"
    # DETAIL_URL = "http://a.xkanba.com/?v={id}"
    DETAIL_URL = "http://www.xkanba.com/?m=vod-play-id-{id}-src-1-num-1.html"
    list_re = re.compile(r'<h3 class="fed-elip"><a href="/\?m=vod-play-id-(.*?)-src-.*?">(.*?)</a></h3>')

    @classmethod
    def search(self, name):
        try:
            print "传入:",name,type(name)
            r = requests.get(self.SEARCH_URL.format(name=quote(name.encode("utf-8"))))
            print r
            html = r.content
            print html
        except Exception as e:
            print e
        else:
            print html
            search_result = self.list_re.findall(html, re.S)
            result = list()
            if search_result:
                for item in search_result:
                    print item[0],item[1]
                    result.append({
                        "ori": self.DETAIL_URL.format(id=item[0]),
                        "name": item[1]
                    })
                return result

if __name__ == "__main__":
    print XkanbaSearch.search("战狼")
