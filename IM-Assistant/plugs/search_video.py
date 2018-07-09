# coding:utf-8

import requests
import json

def search_video(name=""):
    search_url = "http://127.0.0.1:8181/search_video?name={name}"
    video_info = requests.get(search_url.format(name=name))
    content = video_info.content.decode("utf-8")
    return json.loads(content)


def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content.startswith("给我搜"):
        name = content.replace("给我搜","")
        print "-----",name
        info = search_video(name)
        print "info",info
        msg = "@%s\n" % member
        if not info:
            msg += '抱歉，未能寻找到【%s】' % name

            bot.SendTo(contact,msg)
        else:
            for num,item in enumerate(info):
                num += 1
                msg += "%s:%s:%s\n" %(str(num),item['name'].encode("utf-8"),item['ori'].encode("utf-8"))
            bot.SendTo(contact,msg)

    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == "__main__":
    # print onQQMessage(None,None,"",'给我搜 我不是药神')
    from urllib import quote,urlencode
    print quote("/")
    a = urlencode({"long_url":"http://js.dkqapp.cn/68522"})
    import requests

    r = requests.get('http://api.t.sina.com.cn/short_url/shorten.json?source=0a0841d9c1d428bb9c6a1178f3b943c2&%s'% a)
    print r.url