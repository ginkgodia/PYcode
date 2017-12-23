#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/16 10:47
# @Author: Ginkgo
# @File :take_m.py

import pickle


with open('db_name', 'rb') as f:
   dict_account = pickle.loads(f.read())
   # print(type(dict_account))
   print(type(dict_account['10001']['balance']))
   dict_account['10001']['balance'] -= 1000
   print(dict_account)
with open('db_name', 'wb') as f:
    f.write(pickle.dumps(dict_account))


