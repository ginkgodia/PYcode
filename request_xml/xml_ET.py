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
# print(root.tag, root.attrib)
"""
for items in root:
    print(items.tag, items.attrib)
print(root[0].tag)
print(root[0].attrib)
print(root[0].text)
print("=========")
print(root[0][0].tag)
print(root[0][0].attrib)
print(root[0][0].text)
print(root[0][1].tag)

for item in root.iter(tag="book"):
    print(item.tag, item.attrib)

for items in root.iter(tag="title"):
    print(items.tag, items.attrib)
"""
for item in root.iterfind("book/title"):
    print(item.tag, item.text)

for items in root.findall("book"):
    title = items.find("title").text
    price = items.find("price").text
    lang = items.find("title").attrib.get("lang")
    print(title, price, lang)
