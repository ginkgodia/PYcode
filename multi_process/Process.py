#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: Process
# @Time: 2018/1/27 16:07

import threading
import time
# threading.Thread
def work(arg):
    time.sleep(1)
    print(arg)

# for x in range(10):
    # work(x)

for x in range(10):
    threading.Thread(target=work, args=x)