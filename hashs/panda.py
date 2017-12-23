#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/22 0022 10:50
# @File:panda.py
import pickle
from io import StringIO


# s = StringIO()
# s.write('www.baidu.com')
# s.seek(0)
# print(s.read())
# print(s.seek(0))






def init():
    users = {}
    with open("DB", "wb") as f:
        f.write(pickle.dumps(users))


def adduser(arg1, arg2):
    global users
    with open("DB", "rb+") as f:
        users = pickle.loads(f.read())
        users[arg1] = arg2
        print(users)
    with open("DB", "wb") as f:
        f.write(pickle.dumps(users))


def check():
    with open("DB", "rb") as f:
        users = pickle.loads(f.read())
        print(users)


# init()
adduser("adb", "aab")
check()

# �}q X   aqX   bqs.
