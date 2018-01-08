#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2018/1/6 11:13
# @Author: Ginkgo
# @File :create_xml.py

from xml.etree import ElementTree as ET
from xml.dom import minidom
# 创建根节点：
# root = ET.Element("famliy")
'''
# 创建根节点
root = ET.Element("conutry")
# 创建子节点
subroot1 = ET.SubElement(root, "city", attrib={"zz": "NB"})
subroot2 = ET.SubElement(root, "locate", attrib={"north": "cold"})
subroot1.text = "aa"
subroot2.text = "bb"
et = ET.ElementTree(root)
et.write("create.xml", encoding="utf-8", xml_declaration=True)
'''
'''
# 创建子节点
# 利用makeelement
# 每一个节点都是element对象
tree = ET.parse("create.xml")
# 将create.xml装载进tree
root = tree.getroot()
# 获得create.xml的根节点
son = root.makeelement('usa', dict(k1="v1"))
# 创建一个子节点，和root没有逻辑关系
root.append(son)
# 指定创建节点是那个节点的子节点
tree.write("out.xml")
'''
"""
tree = ET.parse("doc.xml")
root = tree.getroot()
print(type(tree))
node1 = ET.Element("en",{"k1":"v1"})
node2 = ET.Element("cn", {"k2": "v2"})
node2.append(node1)
print(type(node2))
root.append(node2)
tree.write("out2.xml")
aa = ET.Element()
bb = ET.ElementTree()
"""

root = ET.Element("tag",attrib={"k1":"v1"})
tree = ET.ElementTree(root)
# tree.write("new.xml")
tree.write("new.xml",encoding="utf-8",short_empty_elements=True)