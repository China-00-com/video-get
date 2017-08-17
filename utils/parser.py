# coding:utf-8

import re
import subprocess
import os


class ConsoleParser(object):
    pass


class ConsoleExec(object):
    @classmethod
    def command_1(cls, command):
        command = map(lambda x: x.strip(), command.split())
        output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()
        return output[0]

    @classmethod
    def command_2(cls, command):
        process = os.popen(command)
        output = process.read()
        process.close()
        return output

    @classmethod
    def get_i(cls, **kwargs):
        pass

    @classmethod
    def get_u(cls, **kwargs):
        pass

    @classmethod
    def download_video(cls, **kwargs):
        pass


if __name__ == "__main__":
    pass
