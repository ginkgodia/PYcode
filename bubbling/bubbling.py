#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/11/27 21:41
# @Author: Ginkgo
# @File :bubbling.py
"""
li = [11, 2, 3, 22]
# print(len(li))
for j in range(1, len(li)):
    for i in range(len(li) - j):
        if li[i] > li[i + 1]:
            temp = li[i]
            li[i] = li[i + 1]
            li[i + 1] = temp
print(li)



li = [11, 2, 3, 22, 4, 2, 4, 11, 341, 314, 13413, 2314, 123, 3]


# def cop(i):
#     if li[i] > li[i + 1]:
#         tmp = li[i]
#         li[i] = li[i + 1]
#         li[i + 1] = tmp
#         return li
#
#
# for i in [0, len(li)-1]:
#     map(cop, li)
# print(li)
"""


def Fib(a, b, depth):
    if depth > 4:
        return a
    c = a + b
    ret = Fib(b, c, depth + 1)
    print(a)
    return ret


ret = Fib(0, 1, 1)
print(ret)
