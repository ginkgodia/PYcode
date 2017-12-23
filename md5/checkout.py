# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/20 22:30
# @Author: Ginkgo
# @File :checkout.py

import pickle


def checkout():
    with open("db", "rb") as f:
        data = pickle.loads(f.read())
        print(data)
        # print(f.read())

checkout()
