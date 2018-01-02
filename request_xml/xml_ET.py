#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2018/1/2 0002 16:39
# @File:xml_ET.py

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

ret = ET.ElementTree(file="doc.xml")
# print(ret)
root = ret.getroot()
print(root.tag, root.attrib)
