#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/20 22:27
# @Author: Ginkgo
# @File :structure.py
import pickle
db = {}

with open("db", "wb") as f:
    f.write(pickle.dumps(db))

