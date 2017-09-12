#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 11.类成员的修饰符之公有私有字段.py
@time: 2017/8/23 下午3:59
@desc:
'''


# 1.有成员和公有成员的定义不同：私有成员命名时，前两个字符是下划线。（特殊成员除外，例如：__init__、__call__、__dict__等）
class C:
    def __init__(self):
        self.name = '公有字段'
        self.__foo = "私有字段"


# 2.普通字段
# (1).公有普通字段
# 公有普通字段：对象可以访问；类内部可以访问；派生类中可以访问
class C:
    def __init__(self):
        self.foo = "公有普通字段"
    def func(self):
        print(self.foo)       #类内部访问
class D(C):
    def show(self):
        print(self.foo)       #派生类中访问

obj = C()
obj_son = D()
# 通过对象访问
print(obj.foo)
# 通过类内部访问
obj.func()
# 通过派生类访问
obj_son.show()


# (2).私有普通字段
class E:
    def __init__(self):
        self.__foo = "私有普通字段"
    def func(self):
        print(self.__foo)       #类内部访问
class F(E):
    def show(self):
        print(self.__foo)       #派生类中访问

obj = E()
obj_son = F()
# 无法通过对象访问
# obj.__foo                     # 错误
# 只能在类内部访问
obj.func()                      # 正确
# 派生类也无法访问
# obj_son.show()                  # 错误