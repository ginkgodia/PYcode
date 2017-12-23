#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/10 0010 17:55
# @File:time.py

import time
#print(time.time())
#print(time.sleep(5))
#print(time.gmtime())
#print(time.ctime())
#print(time.localtime())
#print(time.gmtime())
#t = time.localtime()
#print(time.mktime(t))
#print(time.strftime('%Y-%m-%d %H:%M:%S',t))
#t = time.strptime('2017-12-10 17:03:12','%Y-%m-%d %H:%M:%S')
#print(time.struct_time(t))

#tm_obj = time.localtime()

print("%s-%s" % (time.localtime().tm_year,time.localtime().tm_mon))