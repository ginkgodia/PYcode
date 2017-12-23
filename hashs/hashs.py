#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/19 0019 7:57
# @File:hashs.py

import hashlib
import pickle


def md5(arg):
    t = hashlib.md5(bytes("ad;ddafd;as;", encoding="utf-8"))
    t.update(bytes("arg", encoding="utf-8"))
    return t.hexdigest()


def login(arg1, arg2):
    with open("db", "rb") as f:
        users = pickle.loads(f.read())
        print(users)
        if users[arg1] == md5(arg2):
            print("login success")
        else:
            print("login fail")


def register(arg1, arg2):
    global users
    with open("DB", "rb+") as f:
        users = pickle.loads(f.read())
        users[arg1] = md5(arg2)
        print(users)
    with open("DB", "wb") as f:
        f.write(pickle.dumps(users))


t = input("please input 1 to choose register,2 to login")
if t == "1":
    username = input("Please input your username:")
    password = input("Please input your password:")
    register(username, password)
elif t == "2":
    username = input("Please input your username:")
    password = input("Please input your password:")
    login(username, password)
