#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: s1
# @Time: 2018/1/25 22:00
import socket
import select

s1 = socket.socket()
s1.bind(("127.0.0.1", 8001))
s1.listen()
inputs = [s1, ]
outputs = []
message_dict = {}
while True:
    r_list, w_list, x_list = select.select(inputs, outputs, [], 1)
    print("正在监听%d 个对象" % len(inputs))
    print(r_list)
    for item in w_list:
        item.sendall(bytes(message_dict[item]+"hello", encoding="utf-8"))
        outputs.remove(item)
    for connect_or_obj in r_list:
        print("2")
        if connect_or_obj == s1:
            conn, address = connect_or_obj.accept()
            inputs.append(conn)
        else:
            try:
                re = str(connect_or_obj.recv(1024), encoding="utf-8")
            except Exception as E:
                inputs.remove(connect_or_obj)
            else:
                outputs.append(connect_or_obj)
                message_dict[connect_or_obj] = re
                # connect_or_obj.sendall(bytes(re + "ok", encoding="utf-8"))