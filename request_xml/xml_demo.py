#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2018/1/2 0002 16:21
# @File:xml_demo.py
"""
xml是实现不同语言和程序之间进行数据交换的协议
"""
#解析xml
#检查QQ账号是否在线
from xml.etree import ElementTree as ET
import urllib
import requests
r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=907632998')
result = r.text
node = ET.XML(result)
if node.text == "Y":
    print("online")
else:
    print("offline")
