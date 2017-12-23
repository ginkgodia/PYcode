#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/18 21:57
# @Author: Ginkgo
# @File :md5.py

# from hashlib import md5
#
# hash = md5(bytes("ad;'sadf'as'", encoding="utf8"))
# hash.update(bytes("123456", encoding="utf8"))
# print(hash.hexdigest())


# import hashlib
#
# t = hashlib.md5()
# t.update(bytes("RootAdmin",encoding="utf-8"))
# print(t.hexdigest())

import hashlib
import pickle


def md5(arg):
    hashs = hashlib.md5(bytes("ad;ddafd;as;", encoding="utf-8"))
    hashs.update(bytes(arg, encoding="utf-8"))
    return hashs.hexdigest()


def login(arg1, arg2):
    with open("db", "rb") as f:
        data = pickle.loads(f.read())
        print(data)
        if data[arg1] == md5(arg2):
            print("login success")
        else:
            print("login fail")


def register(arg1, arg2):
    with open("db", "rb+") as f:
        # f.seek(0)
        adata = pickle.loads(f.read())
        adata[arg1] = md5(arg2)
        print(adata)
        f.write(pickle.dumps(adata))


t = input("please input 1 to choose register,2 to login")
if t == "1":
    username = input("Please input your username:")
    password = input("Please input your password:")
    register(username, password)
elif t == "2":
    username = input("Please input your username:")
    password = input("Please input your password:")
    login(username, password)
