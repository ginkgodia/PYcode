#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2018/1/6 10:41
# @Author: Ginkgo
# @File :xml_write.py

from xml.etree import ElementTree as ET

ret = ET.parse("doc.xml")
root = ret.getroot()
# print(root)
for node in root.iter("book"):
    # print(node.attrib)
    # for node_node in node.iter("title"):
    for node_node in node.iter("year"):
        # print(node_node.text)
        # node_node.text = node_node.text + "aab"
        years = int(node_node.text)
        node_node.text = str(years+1)
        print(node_node.text)
        node_node.set("k1", "v1")
        print(node_node.attrib)

ret.write("doc.xml")