#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: server
# @Time: 2018/1/25 20:49

import socket
import select
s1 = socket.socket()
s1.bind(("127.0.0.1", 8001))
s1.listen()
s2 = socket.socket()
s2.bind(("127.0.0.1", 8002))
s2.listen()
s3 = socket.socket()
s3.bind(("127.0.0.1", 8003))
s3.listen()

inp = [s1, s2, s3, ]
while True:
    """
    select 方法监听inp中的三个对象s1, s2, s3，如果那个对象发生变化，将其写入
    r_list中，如果那个错误，将其加入x_list中，w_list获取中间参数的值，无论是否发生变化
    """
    r_list, w_list, x_list = select.select(inp, [], [], 1)
    print(r_list)
    for item in r_list:
        con, address = item.accept()
        print(address)
        con.sendall(bytes("address", encoding="utf-8"))
