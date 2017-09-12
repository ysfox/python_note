#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 14.类的特殊成员.py
@time: 2017/8/24 上午11:09
@desc:
'''


class Foo:
    """ 描述类信息可以通过__doc__打印出来 """
    country = "公共静态字段"
    def __init__(self, sq = [1, 2, 3, 4]):
        self.name = "公共普通字段"
        self.sq = sq
        print("对象初始化时执行方法")

    def __def__(self):
        print("对象释放时执行放方法，由编译器释放内存时自动调用")

    def __call__(self, *args, **kwargs):
        print("此方法由对象后面加括号触发执行")

    def __str__(self):
        return("打印对象时候将打印此方法返回的值")

    def __getitem__(self, key):
        print("__getitem__方法执行", key)

    def __setitem__(self, key, value):
        print("__setitem__方法执行", key, value)

    def __delitem__(self, key):
        print("__delitem__方法执行", key)

    # 此方法好像失效
    def __setslice__(self, i, j, sequence):
        print("__setslice__方法执行", i, j)

    # 此方法好像失效
    def __getslice__(self, i, j):
        print("__getslice__方法执行", i, j)

    # 此方法好像失效
    def __delslice__(self, i, j):
        print("__delslice__方法执行", i, j)

    # 有此方法并返回可迭代对象则可迭代
    def __iter__(self):
        return iter(self.sq)

    def func(self):
        pass

foo = Foo()
# 1. __doc__   表示类的描述信息
print(Foo.__doc__)


# 2. __module__ 表示当前操作的对象在那个模块
print(foo.__module__)


# 3. __class__ 表示当前操作的对象的类是什么
print(foo.__class__)


# 4. __init__ 构造方法，创建对象时自动触发执行
Foo()             #创建对象时自动触发__init__


# 5. __del__  析构方法，当对象在内存中释放时候自动触发
# 此方法一般无须定义，因为析构函数的调用是由解释器进行垃圾回收时自动调用是


# 6. __call__  对象后面加括号触发执行
foo()                   #__call__方法的执行是由对象后加括号触发的


# 7. __dict__ 类或对象中的所有成员
# 注意类的普通字段属于对象，类中的静态字段和方法属于类
print(Foo.__dict__)
print(foo.__dict__)


# 8. __str__ 打印对象时将打印此方法返回的值
print(foo)


# 9.__setitem__,__getitem__,__delitem__ 用于索引操作，分别表示设置，获取和删除
foo['key'] = "alex"           # 自动触发执行 __setitem__
print(foo['key'])             # 自动触发执行 __getitem__
del foo['key']                # 自动触发执行 __delitem__


# 10.__getslice__、__setslice__、__delslice__ python2中该三个方法用于分片操作
# python3中为__getitem__、__setitem__、__delitem__ 传入只类型被转换成<class 'slice'>
foo[0:1] = [11, 22, 33, 44]    # 自动触发执行 __setslice__
foo[-1:1]                      # 自动触发执行 __getslice__
del foo[0:2]                   # 自动触发执行 __delslice__


# 11. __iter__ 用于迭代器，之所以列表、字典、元组可以进行for循环，是因为类型内部定义了 __iter__
for i in foo:
    print(i)




