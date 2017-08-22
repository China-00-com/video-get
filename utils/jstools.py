# coding:utf-8


import sys
import os
import requests
from pkg_resources import resource_filename


def closure_js(name):
    name = name
    jar_file_name = resource_filename(__name__, "closure.jar")
    os.execlp("java", name, "-jar", jar_file_name)


# https://developers.google.com/closure/compiler/docs/gettingstarted_api



if __name__ == "__main__":
    closure_js("test.js")
