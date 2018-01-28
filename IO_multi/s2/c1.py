#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: c1
# @Time: 2018/1/25 22:12


import socket

c1 = socket.socket()
c1.connect(("127.0.0.1", 8001,))
while True:
    inp = input("请输入要说的话：\n >>>>")
    c1.sendall(bytes(inp, encoding="utf-8"))
    st1 = str(c1.recv(1024), encoding="utf-8")
    print(st1)
c1.close()