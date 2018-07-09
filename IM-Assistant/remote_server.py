# coding:utf-8

import os
from flask import Flask, request,jsonify
from itsdangerous import SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from spider import XkanbaSearch
app = Flask(__name__)

SECRET_KEY = "This is SECRET_KEY"


def encode_token(url="", expiration=24 * 60 * 60):  # 秒, 30天过期
    token_s = Serializer(SECRET_KEY, expires_in=expiration)
    return token_s.dumps({'ori': url})


def decode_token(token):
    serializer = Serializer(SECRET_KEY)
    try:
        ver_info = serializer.loads(token)
        ori = ver_info.get("ori", "")
    except SignatureExpired as e:
        pass
    except BadSignature as e:
        pass
    except Exception as e:
        pass
    else:
        return ori


@app.route("/search_video")
def transe():
    name = request.args.get('name')
    print "name:",name
    search_result = XkanbaSearch.search(name)
    print "search:",search_result
    if not search_result:
        search_result = dict()
    return jsonify(search_result)


if __name__ == "__main__":
    os.system("cp ./plugs/*.py ~/.qqbot-tmp/plugins/")
    app.run(host="0.0.0.0", port=8181, threaded=True)
    # print encode_token('http://www.baidu.com')