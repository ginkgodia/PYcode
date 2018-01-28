#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: server
# @Time: 2018/1/24 22:28

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import conf.setting
import socketserver
from lib.modules import *
import subprocess

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
    server.serve_forever()
