#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/11/28 19:14
# @Author: Ginkgo
# @File :decorator.py
"""
def outer(func):
    def inner():
        print("hello")
        print("hello")
        print("hello")
        print("hello")
        r = func()
        print("End")
        print("End")
        print("End")
        return r
    return inner

@outer
def f1():
    print("F1")


def f2():
    print("F2")


def f3():
    print("F3")


def f4():
    print("F4")


f1()

"""


def decorator(func):
    def inner():
        print("OKOKOK")
        print("OKOKOK")
        r = func()
        print("ONT")
        print("ONT")
        return r

    return inner()


@decorator
# 1、当python 执行程序遇到装饰器时，会将@decorator 下边的函数名作为装饰器函数的参数
#   进行执行，并将其结果返回给函数 f1 = inner()
def f1():
    print("F1")
