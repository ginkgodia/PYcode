#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: client
# @Time: 2018/1/24 22:28

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import conf.setting
import socket, socket
cli = socket.socket()
cli.connect(("127.0.0.1", 9000))
ret = str(cli.recv(1024), encoding="utf-8")
print(ret)
inp = input("请输入您的选择： 1，注册，2，登录 \n >>>")
inp1 = input("请输入用户名：")
cli.sendall(bytes(inp1, encoding="utf-8"))
print(str(cli.recv(1024), encoding="utf-8"))
inp2 = input("请输入密码：")
cli.sendall(bytes(inp2, encoding="utf-8"))
print(str(cli.recv(1024), encoding="utf-8"))
print("+++++++++")
cli.sendall(bytes(inp, encoding="utf-8"))
print(str(cli.recv(1024), encoding="utf-8"))
print(str(cli.recv(1024), encoding="utf-8"))

while True:
    command = input("请输入要执行的命令：")
    cli.sendall(bytes(command, encoding="utf-8"))
    command = str(cli.recv(1024), encoding="utf-8")
    result = str(cli.recv(1024), encoding="utf-8")
    print(command, "\n", result)