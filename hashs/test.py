#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/21 0021 9:04
# @File:test.py

import pickle


def login(arg1, arg2):
    with open("db", "rb+") as f:
        data = pickle.loads(f.read())
        data[arg1] = arg2
        print(data)
        f.write(pickle.dumps(data))


login("a", "b")
