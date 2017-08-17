# coding:utf-8

import os

SETTINGS = dict()

SETTINGS["blog_title"] = u"Tornado Blog"
print os.path.realpath(__file__)
SETTINGS["template_path"] = os.path.join(os.path.dirname(__file__), "../templates")
SETTINGS["static_path"] = os.path.join(os.path.dirname(__file__), "../static")
SETTINGS["debug"] = True
# SETTINGS["ui_modules"]={"Entry": EntryModule},
# SETTINGS["xsrf_cookies"]=True,
# SETTINGS["cookie_secret"]="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
# SETTINGS["login_url"]="/auth/login",
