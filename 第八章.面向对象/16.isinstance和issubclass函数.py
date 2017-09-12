#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 16.isinstance和issubclass函数.py
@time: 2017/8/25 上午11:08
@desc:
'''


class Foo(object):
    pass
class Bar(Foo):
    pass

# 一、isinstance(obj, cls),检查obj是否是类 cls 的对象
obj = Foo()
print(isinstance(obj, Foo))

# 二、issubclass(sub, super),检查sub类是否是 super 类的派生类
print(issubclass(Bar, Foo))