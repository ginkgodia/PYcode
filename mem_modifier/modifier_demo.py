#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: modifier_demo
# @Time: 2018/1/15 22:01

"""
class Foo():
    __name = "Tommy"
    def __init__(self):
        self.__key = "value"
    def Fo(self):
        print("普通方法")
        print(self.__key)
    def __Fo(self):
        print("修饰的方法")
    @staticmethod
    def Fo1():
        print("staticmethod")
        print(Foo.__name)
    @staticmethod
    def __Fo2():
        print("装饰后的静态方法")
    @classmethod
    def Fo3(cls):
        print(cls)
        Foo.__Fo2()

    @property
    def Fo4(self):
        print("property")
    @property
    def __Fo5(self):
        print("装饰后的特性")

# print(Foo.__name) 错误调用，私有字段，无法在类之外调用
# Foo.Fo1()
Foo.Fo3()
obj = Foo()
# obj.Fo3()
# obj.Fo4
class B:
    def __init__(self):
        print("init")
    def __call__(self, *args, **kwargs):
        print("call")
        return "A"
B1 = B()
ret = B1()
print(ret)

# or
ret2 = B()()
print(ret2)

class A:
    def __init__(self):
        pass
    def __getitem__(self, item):
        print(item, type(item), "getitem")

A1 = A()
A1[1:10]
"""

class C:
    def __init__(self):
        pass
    def __iter__(self):
        yield 1
        yield 2
        yield 3
c1 = C()
for i in c1:
    print(i)