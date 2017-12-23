#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/11/29 22:00
# @Author: Ginkgo
# @File :decorator1.py


def decorator(func):
    def inner1(*args, **kwargs):
        print("OK")
        r = func(*args, **kwargs)
        print("SS")
        return r

    return inner1


def decorator1(func):
    def inner2(*args, **kwargs):
        print("OK!")
        r = func(*args, **kwargs)
        return r

    return inner2


@decorator1
@decorator
def f1(a1, a2):
    print(a1 + a2)

f1(1, 2)
