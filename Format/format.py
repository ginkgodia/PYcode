#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/12/23 0023 15:35
# @File:format.py
# 格式化： %
# %[(name)][flag][width].[precision]codetype
# print("ginkgo is a %s man ,he is %d years old" % ("great", 20))
# s = "ginkgo is a %s man ,he is %d years old" % ("great", 20)
# s = "ginkgo is a %(n1)s man ,he is %(n2)d years old" % {"n1":"great","n2":20}
# s = "ginkgo is a %(n1)-10s man ,he is %(n2)-5d years old" % {"n1":"great","n2":-20}
# s = "ginkgo is a %(n1)-6s man ,he is %(n2)5.3f years old" % {"n1":"great","n2": 20.0000}
# print(s)
# s = "you are a %c" % 244
# print(s)

# s = "The process is complete %d%%" % 20
# print(s)
# format
# [[fill]align][sign][#][0][width][,][.precision][type]
# s = "a is {:#=10} boy ".format(-100)
# print(s)
# s = "The loading process is {:.2%}".format(0.2)
# print(s)
# s = "i am {0},you are {1}".format("a","b")
# s = "i am {0},you are {0}".format(*["a", "b"])
# s = "i am {older},you are {younger}".format(**{"younger":"a", "older":"b"})
s = "numbers: {:b},{:o},{:d},{:x},{:X},{:.2f} {:.2%}".format(15, 15, 15, 15, 15, 15.87623, .2)
print(s)