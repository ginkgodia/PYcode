#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/21 0021 8:41
# @File:check.py

try:
    import cPickle as pickle
except ImportError:
    import pickle


def check():
    with open("DB", "rb") as f:
        users = pickle.loads(f.read())
        print(users)


check()
