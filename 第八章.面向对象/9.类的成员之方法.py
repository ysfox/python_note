#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 9.类的成员之方法.py
@time: 2017/8/23 下午3:48
@desc:
'''


# 1.方法
# 方法包括：普通方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同。
# 普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；
# 类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；
# 静态方法：由类调用；无默认参数；

class Foo:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """
        print('普通方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""
        print('静态方法')


f = Foo("alex")
# 调用普通方法
f.ord_func()
# 调用类方法
Foo.class_func()
# 调用静态方法
Foo.static_func()