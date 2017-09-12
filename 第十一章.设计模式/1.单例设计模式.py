#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.单例设计模式.py
@time: 2017/8/25 下午2:19
@desc:
'''


# 1.单例设计模式
# 单利模式存在的目的是保证当前内存中仅存在单个实例，避免内存浪费！！！

class Foo(object):
    __instance = None

    @staticmethod
    def singleton():
        if Foo.__instance:
            return Foo.__instance
        else:
            Foo.__instance = Foo()
            return Foo.__instance

# 对于Python单例模式，创建对象时不能再直接使用：obj = Foo()，而应该调用特殊的方法：obj = Foo.singleton()
obj = Foo.singleton()

