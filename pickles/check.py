#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/16 10:53
# @Author: Ginkgo
# @File :check.py

import pickle

with open('db_name', 'rb') as f:
    t = pickle.loads(f.read())
    print(t)