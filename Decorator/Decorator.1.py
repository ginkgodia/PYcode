#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/11/28 23:25
# @Author: Ginkgo
# @File :Decorator.1.py


def add_func(func):
    def inner(*args, **kwargs):
        print("Welcome you")
        ret = func(*args, **kwargs)
        print("Bye bye ")
        return ret

    return inner


@add_func
def base_func1(a1, a2):
    print("IT is T1")
    return a1 + a2


@add_func
def base_func2():
    print("IT is T2")


@add_func
def base_func3():
    print("IT is T3")


print(base_func1(1, 2))
base_func2()
base_func3()
