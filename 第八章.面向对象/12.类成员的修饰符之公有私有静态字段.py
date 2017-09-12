#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 12.类成员的修饰符之公有私有静态字段.py
@time: 2017/8/24 上午10:32
@desc:
'''


# 1.类成员的修饰符
# 私有成员和公有成员的定义不同：私有成员命名时，前两个字符是下划线。（特殊成员除外，例如：__init__、__call__、__dict__等）
class C:
    def __init__(self):
        self.name = '公有字段'
        self.__foo = "私有字段"

# 1.静态字段
# (1).公有静态字段
# 公有静态字段：类可以访问；类内部可以访问；派生类中可以访问
class C:
    name = "公共静态字段"
    def func(self):
        print(C.name)
class D(C):
    def show(self):
        print(C.name)

# 类访问
print(C.name)
# 类内部可以访问
obj= C()
obj.func()
# 派生类中可以访问
obj_son = D()
obj_son.show()


# (2).私有静态字段
# 私有静态字段：仅类内部可以访问；
class C:
    __name = "私有静态字段"
    def func(self):
        print(C.__name)
class D(C):
    def show(self):
        print(C.__name)

# 不能通过类直接访问
# print(C.__name)       #错误
# 只能在类内部访问
obj = C()
obj.func()
# 也不能再派生类中访问
obj_son = D()
# obj_son.show()        #错误
