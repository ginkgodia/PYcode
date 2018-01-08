#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @version:python3.7
# @Author:Ginkgo
# @file:config_demo.py
# @time:2018/1/8 23:11

import configparser
"""
cp = configparser.ConfigParser()
#cp对象的read功能，打开文件并读取文件，放到内存中
cp.read("php.ini", encoding="utf-8")
#con 对象的sections 方法，在内存中寻找所有的[xx]字段
res = cp.sections()
ret = cp.options("name")
print(res, ret)
"""

conf = configparser.ConfigParser()
conf.read("php.ini", encoding="utf-8")
res = conf.sections()
print(res)

ret = conf.items("name")
print(ret)

re = conf.options("name")
print(re)

rs = conf.get("name", "jinkeen")
print(rs)

rs1 = conf.getint("name", "num")
print(rs1)
rs2 = conf.getfloat("name","num")
print(rs2)

has = conf.has_section("name")
print(has)
has_i = conf.has_option("name","num")
print(has_i)

conf.add_section("sec")
conf.remove_section("sec")
conf.write(open("php.ini","w"))
has_opt = conf.has_option("name", "jinkeen")
print(has_opt)
rem = conf.remove_option("name", "jinkeen")
add = conf.set("name", "hel","111")
conf.write(open("php.ini","w"))

