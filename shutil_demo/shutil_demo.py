#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: shutil_demo
# @Time: 2018/1/9 19:54

import shutil
# shutil.copyfileobj(open("../request_xml/out.xml","r"), open("a.xml", "w"))
# shutil.copyfile("../request_xml/out.xml", "b.xml")
# shutil.copymode("a.xml", "b.xml")
# shutil.copystat("a.xml", "b.xml")
# shutil.copy("a.xml", "c.xml")
# shutil.copy2("a.xml", "d.xml")
# shutil.copytree("../request_xml", "test", symlinks=False, ignore=shutil.ignore_patterns("*.pyc", "tmp.*"))
# shutil.rmtree("test", ignore_errors=True)
# shutil.move("a.xml", "x.xml")
# shutil.make_archive("request", "zip", root_dir="../request_xml/", owner="root", group="root" )
# import zipfile
# z = zipfile.ZipFile("request.zip","w")
# z.write("x.xml")
# # z.close()
# z.extract("x.xml")
# z.extractall()
# z.close()
shutil.copyfile("b.xml","c.xml")