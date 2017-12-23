#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/21 0021 8:39
# @File:init.py
try:
    import cPickle as pickle
except ImportError:
    import pickle

def init():
    users = {}
    with open("DB", "wb") as f:
        f.write(pickle.dumps(users))


init()
