#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: Error_solve
# @Time: 2018/1/16 0:01

"""
try:
    inp = int(input("请输入数字:"))
    print(inp)
except Exception as E:
    print("数字类型错误")
"""

# 对不同的错误有不同的错误类型，包括：IndexError, ValueError ，但这些类都是
# exception类的派生类，可能是子类或者更下一级的类
# 对于不确定的错误信息，可以先尝试用已知的错误类型捕捉，在捕捉不到的时候
# 使用Exception 错误来接收
"""
try:
    li = []
    print(li["aab"])
except IndexError as E:
    print(E)
except TypeError as E:
    print(E)
except Exception as E:
    print(E)
"""

# 标准的错误触发流程
"""
try:
    li = []
    print(li[123])
except IndexError as E:
    pass
# 如果触发了错误，那么执行Except，可以有多个
except Exception as E:
    pass
else:
    # 如果没有错误，执行else
    print("OK")

finally:
    # 无论是否触发错误，都会执行finally
    print("find")
    
#　流程：
# 1. 正确流程：
#    执行try， 正常执行，没有触发错误，执行else语句，然后执行finally语句
# 2. 错误流程
#    执行try, 出现错误，执行except语句，依次执行找到符合的错误类型捕获，
#    否则，执行到Except结束，然后执行finally

"""
# 主动触发异常

try:
    print("aaaa")
    raise Exception("Error, test....")
#  主动触发一个错误，并将该错误传递传递给Exception类中，Exception类将
#  该错误信息输送到except 中，作为E 出现
except Exception as E :
    print(E)