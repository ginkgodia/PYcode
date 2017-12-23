# -*- coding=utf8 -*-
"""
f = open("ha.log", "w")
f.write("ha.log")
f.close()

f = open("ha.log", "r+")
print(f.tell())
# f.write("hb.log")
# f.flush()
data = f.read()
f.close()
print(data)

f = open("ha.log", "r+", encoding="utf-8")
data = f.read()
print(type(data), data)
print(f.tell())
f.write("富国人")
print(f.tell())
f.flush()
print(f.tell())
f.seek(0)
data2 = f.read()
f.close()
print(data2)
"""

f = open("ha.log", "r+", encoding="utf-8")
print(f.tell())  # 0
data0 = f.read(2)
f.write("f国人")
print(f.tell())  # 9
data = f.read()
print(f.tell())  # 9
f.seek(0)
print(f.tell())  # 0
data1 = f.read()
f.close()
print(data0, "==", data, "===", data1)


"""
f = open("ha.log", "w+")
print(f.tell())
data = f.read()
print(f.tell())
f.write('hahn')
print(f.tell())
# f.seek(0)
data2 = f.read()
f.close()
print(data, "===", data2)

f = open("ha.log", "a+")
f.seek(0)
data = f.read()
f.close()
print(data)
"""
"""
with open("ha.log", "r+", encoding="utf-8") as f1, open("hb.log", "w+") as f2:
    for line in f1:
        f2.write(line)

"""

"""
def MyMap(func, args):
    list1 = []
    for items in args:
        ret = f1(items)
        list1.append(ret)
    return list1


def f1(x):
    # x = x + 100
    return x+100


ret = MyMap(f1, [11, 22, 33])
print(ret)

"""