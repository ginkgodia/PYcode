#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: logger_demo
# @Time: 2018/1/9 23:58

import logging
logging.basicConfig(filename="out.log",
                    format=("%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(message)s"),
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.DEBUG)
# 只有日志等级大于设定的日志等级时才会写入
logging.debug("debug")
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
# 自己指定日志等级
logging.log(10, 'log')
"""
日志等级：
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
"""
# format.link = https://images2015.cnblogs.com/blog/425762/201605/425762-20160524044013866-178249755.png

# 对于多日志写入：
# 多日志记录，logging.basicConfig无法满足要求，可以根据需要自己设定

# 定制日志写入文件
file1 = logging.FileHandler("file1.log","a",encoding="utf-8")
# 定制日志写入格式
fmt = logging.Formatter(fmt = "%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")

file2 = logging.FileHandler("file2.log","a",encoding="utf-8")
fmt = logging.Formatter()
file2.setFormatter(fmt)

# 定义日志：
logger1 = logging.Logger("s1",level=logging.ERROR)
logger1.addHandler(file1)
logger1.addHandler(file2)

# 写日志
logger1.critical("111")