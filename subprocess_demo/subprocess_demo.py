#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: subprocess_demo
# @Time: 2018/1/9 23:04

import subprocess

# subprocess.call(["ipconfig" ], shell=False)
# subprocess.call("dir", shell=True)
# ret = subprocess.check_call(["ipconfig"])
# print(ret)
# rets = subprocess.check_output(["ipconfig"])
# print(rets)
# subprocess.Popen(["mkdir", "test"])
"""
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')
obj.stdin.write('print 2 \n ')
obj.stdin.write('print 3 \n ')
obj.stdin.write('print 4 \n ')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()
# ===

import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')
obj.stdin.write('print 2 \n ')
obj.stdin.write('print 3 \n ')
obj.stdin.write('print 4 \n ')

out_error_list = obj.communicate()
print out_error_list
# ===
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out_error_list = obj.communicate('print "hello"')
print out_error_list

"""
subprocess.check_call("exit -1", shell=True)