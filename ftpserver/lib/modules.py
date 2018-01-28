#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: modules
# @Time: 2018/1/24 22:31
from hashlib import md5
import socketserver
import  pickle , os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import modules
import subprocess
from conf import  setting

class HashFun:
    def __init__(self):
        self.__string = "ad';"

    def md5(self, tohash):
        self.tohash = tohash
        hash1 = md5(bytes(self.__string, encoding="utf-8"))
        hash1.update(bytes(self.tohash, encoding="utf-8"))
        return hash1.hexdigest()

class Student:
    def __init__(self):
        self.name = None
        self.password = None
    def register(self, name, password):
        self.name = name
        self.password = HashFun().md5(password)
        pickle.dump(self, open(os.path.join(setting.DB_DIR, name), "wb"))
    def login(self, name, password):
        s_obj = pickle.load(open(os.path.join(setting.DB_DIR, name), "rb"))
        if s_obj.name == name and s_obj.password == HashFun().md5(password):

            # print("登录成功")
            return "登录成功"
        else:

            # print("登录失败")
            return "登录失败"
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        con = self.request
        con.sendall(bytes("hello, please login or register", encoding="utf-8"))
        username = str(con.recv(1024), encoding="utf-8")
        con.sendall(bytes("用户名是"+username, encoding="utf-8"))
        print(username)
        password = str(con.recv(1024), encoding="utf-8")
        con.sendall(bytes("密码是"+password, encoding="utf-8"))
        print(password)
        sel = str(con.recv(1024), encoding="utf-8")
        if sel == "1":
            con.sendall(bytes("您输入的是注册：", encoding="utf-8"))
            Student().register(username, password)
        elif sel == "2":
            con.sendall(bytes("您输入的是登录：", encoding="utf-8"))
            if Student().login(username, password) == "登录成功":
                con.sendall(bytes("登录成功", encoding="utf-8"))
                while True:
                    ret = str(con.recv(1024), encoding="utf-8")
                    con.sendall(bytes("您输入的命令是"+ret, encoding="utf-8"))
                    if ret == "q":
                        break
                    else:
                        exec_result = subprocess.getoutput(ret)
                    con.sendall(bytes(exec_result, encoding="utf-8"))
            else:
                con.sendall(bytes("登录失败，请重新登录", encoding="utf-8"))


