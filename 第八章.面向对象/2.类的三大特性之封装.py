#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 2.类的三大特性之封装.py
@time: 2017/8/23 上午10:10
@desc:
'''


# 1.面向对象三大特性之封装
# 一、封装
class Foo2:
    #构造方法，类创建对象时自动执行
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


# 内容其实被封装到了对象 obj1 和 obj2 中，每个对象中都有 name 和 age 属性
obj1 = Foo2('wupeiqi', 18)
print(obj1.name)    # 直接调用obj1对象的name属性
print(obj1.age)     # 直接调用obj1对象的age属性
obj1.detail()       # Python默认会将obj1传给self参数，即：obj1.detail(obj1)，所以，此时方法内部的 self ＝ obj1

obj2 = Foo2('alex', 78)
print(obj2.name)    # 直接调用obj2对象的name属性
print(obj2.age)     # 直接调用obj2对象的age属性
obj2.detail()       # Python默认会将obj2传给self参数，即：obj2.detail(obj2)，所以，此时方法内部的 self ＝ obj2