#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: oop
# @Time: 2018/1/11 23:22

"""
# 面向对象
class filter:
    def func1(self, arg1):
        print(arg1, self)
    def func2(self, arg2):
        return arg2

obj1 = filter()
ret = obj1.func1("a")
print(obj1)
"""

"""
注解：
    当程序执行到类时，会在内存空间中创建一个类，包括类名和其中的方法
    当由类创建实例时，同样会在内存空间中生成对应实例的空间和一个类对象指针。
    这个指针指向创建该实例的类。
    类相当于把一些方法进行了封装
"""
"""
self 注解：
    当由类创建了实例后， 实例在内存中生成一个实例对应的对象和一个类对象指针
    当实例调用类的方法时，python 会默认给类中的方法传递一个self形参
    self形参在内存中的地址和由调用该方法的实例所指向的地址是一致的。
    
"""


# 面向对象的封装
# 一般情况下如此类
class A:
    def func1(self, AA):
        print(AA)

    def func2(self, AA, BB):
        print(AA, BB)

    def func3(self, AA, CC):
        print(AA, CC)


obj1 = A()

# 但是由于有太多的重复参数，可用将这些重复的参数封装到由类创建的实例中
# 而在类中创建方法的时候，python会自动生成一个self 形参
# self 形参和由类创建的对象时指向同一个内存地址
# 因此，对实例进行封装后，self 就具有了和实例一样的参数，这样就避免了重复输入
"""
class B:
    def func1(self):
        print(self.AA)
    def func2(self, BB):
        print(self.AA, BB)
    def func3(self, CC):
        print(CC)
obj2 = B()
obj2.AA = "hello"
obj2.func1()
obj2.func2("best")
"""


# 由结果可见，封装后使用的方便性提高了
#########
# 但是一般情况下，并不通过这种方式进行封装，因为还有另外一种方法更加优秀
# 在利用class创建实例的时候，B()表示执行类B的一个方法
# 这个方法就是__init__方法，有关封装的信息可用放在__init__方法中
"""
class B:
    def __init__(self, bbb):
        self.a = "aaa"
        self.b = bbb

    def K(self, ccc):
        print(self.a, self.b, ccc)


objB = B("BBB")
objB.K("ccc")
"""
# class B()中的__init__(self)方法叫做构造方法，在类创建对象的时候会自动执行
########
# 在什么情况下需要使用类的封装功能：
# 1. 类中不同的方法有共同的参数，可以将其直接封装到对象中
# 2. 把类作为模版，创建多个不同的对象时(对象的属性可以不同)
#######
# 继承：
# 1. 继承使用class A(父类)：的方法进行
# 2. 继承者(子类，派生类) 拥有父类(基类)的所有内容
# 3. 继承中方法在当前类中和父类中都存在，那么当前类生效。
# 4. 继承中的多继承(c,java 不存在)
# 5. 多继承的优先级： 类本身，继承父类(按从左往右排优先级)
# 6. 当当前子类有继承多个父类，不同父类又有相同的父类时，调用函数的优先级是
#     当执行到顶级类之前，会在顶级类执行之前把所有的子类执行

#####
# 多态：
# 多态在python 中意义不大，因为python中的数据都是弱类型的。

###执行基类的构造方法
# 由于在子类和父类(基类)中都可以定义构造方法，但是，当对父类进行继承的时候，
# 是不能，调用类名()生成实例时，只会执行当前类的构造方法，要想同时执行父类的构造方法，需要如下做
# 有两种方法来调用父类的构造方法：
# 1. 使用super函数
#     super(想要调用父类的类名，self).__init__()
# 2. 直接调用父类的方法
#     要调用父类的类名.__init__(self)
# 推荐使用第一种

"""
class Animal():
    def __init__(self):
        self.a = "bear"
        print(self.a)
class Persion(Animal):
    def __init__(self):
        self.tty = "red"
        print(self.tty)
class China(Persion):
    def __init__(self):
        self.color = "black"
        super(Persion, self).__init__()
        # Persion.__init__(self)
        print(self.color)
Jin = China()
print(Jin.__dict__)
"""


class Province:
    # 静态字段
    country = "China"

    def __init__(self, name):
        # 普通字段
        self.name = name

    # 普通方法
    def locate(self):
        pass

    # 静态方法
    @staticmethod
    def Class():
        pass
    # 类方法
    @classmethod
    def PO1(cls):
        print(cls)
    @property
    def PO2(self):
        temp = "Province is %s" % self.name
        print( temp)

    @PO2.setter
    def PO2(self, value):
        print(value)
# Province.PO1()
Heinan = Province("henan")
ret = Heinan.PO2

Heinan.PO2 = "jinkeen"
# print(Province.country, Heinan.name)
# Heibei = Province("hebei")
# print(Province.country, Heibei.name)
# 当存在多个对象调用类中的一个相同的字段时，如果将字段设为普通字段，那么
# 在每个对象创建时都会生成该字段，并将其封装到对象中，会造成大量的内存浪费
# 如果将字段设为静态字段，那么我们知道，当执行类名()创建对象时，就会执行
# 类的初始化函数(__init__) 在内存中生成一个对象和一个类对象指针，如果将字段
# 定义在类中，那么，每次生成的对象就会少占用内存。
#*******************
# 规范
#*******************
# 1. 类中的静态字段、方法和类方法通过类来访问
# 2. 类中的普通字段和方法通过对象来访问
# 3. 获取特性，设置特性即(propery)都是通过对象来进行的，也就是说方法中含有
#    (self)参数时，都要用对象来获取


# 类中的静态方法的作用：
# 在不创建对象的情况下使用这个方法，类似于函数，和是否创建对象无关

# 类方法：
# 类方法可以自动输入所执行的类的名字

# 特性：
# 为方法加上@proprety,其特性是可以将其伪装成字段执行，不用加()来执行函数，前提是该函数不需要传入参数
