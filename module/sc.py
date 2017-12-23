#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/10 23:50
# @Author: Ginkgo
# @File :sc

import os
import sys
import time
# print(sys.path)
for i in range(10):
    s = ""
    if i % 10 == 0:
        print(str(i) + "%")

    else:
        t = sys.stdout.write("#")
        s = s + str(t)
        print(s)
        # t = sys.stdin.read()
        # print(t)
        time.sleep(0.3)

