**成员修饰符**
python 中的成员有：
"""
静态字段
普通字段
静态方法 @staticmethod
普通方法
类方法   @classmethod
特性     @property
"""
成员修饰器就是在成员名称前边加__.
成员修饰器的作用是让不是在类内部的对象无法调用
成员修饰器添加到成员前边时，只有当前的类可用调用该成员，其他类无法调用，
包括继承他的子类

**私有成员不给除自己类以外的的对象使用，但是可以强行访问**
方法：
_Foo__name 即：_类名__私有成员名来访问。

**python中的特殊方法**

- __init__(self) 构造方法，负责在创建对象时执行
- __del__(self)  析构方法，负责解释器在结束时销毁对象
- __call__(self) '调用方法'，负责在实例后执行添加()，执行方法
- __setitem(self, key, value)  当执行obj[aa]="bb" 时，接收key 和value，进行操作，操作内容自己定义
- __getitem(self, item)  当执行obj[aa] 时，接收item参数，执行自定义的设置操作
- __delitem(self, key)  当执行del obj[aa] 时，接收key参数，执行自定义的删除操作
```python
class B:
    def __init__(self):
        print("init")
    def __call__(self, *args, **kwargs):
        print("call")
        return "A"
    def __setitem__(self, key, value):
        print(key, value)
    def __getitem__(self, item):
        print(item)
    def __delitem__(self, key):
        print(key)
B1 = B()
B1()
#或者直接执行
ret = B()()  
print(ret)
#输出结果为init  call A
```

  "__setitem__，__getitem__，__delitem__操作类比dict的设置，获取，删除操作"
  "在python中，无论是对字典进行获取，删除，设置操作，还是对列表进行切片，替换，
  和删除操作，都会执行getitem,setitem,delitem 方法，所不同的是，当对列表执行切片操作
  时，会将列表传入的起始步，结束布和步长作为参数传给一个函数，由该函数封装后传递给item方法"
  
  
```python
class A:
    def __init__(self):
        pass
    def __getitem__(self, item):
        print(item, type(item), "getitem")

A1 = A()
A1[1:10]
# result >slice(1, 10, None) <class 'slice'> getitem
```
"　A1[1:10:2]   ==> getslice(2.7版本)/getitem(>3版本)
   A1[1:5] = ["aa","bb"，"cc"] ==>setslice/setitem
   del A1[1:5]   ==> delslice/delitem
   "
   
"""
__dict__方法
对象.__dict__ 获取对象的所有属性
类.__dict__获取类的所有属性
"""
"""
__iter__方法 迭代器
一个生成器独自无法输出信息，当一个迭代器和生成器组合在一块时，就可以持续输出
"""

```python
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
    
# result > 1 2 3
```