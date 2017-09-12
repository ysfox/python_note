#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 8.多层装饰器.py
@time: 2017/8/29 下午2:29
@desc:
'''

# 多层装饰器(一个函数被多个装饰器装饰)
# 注意执行的顺序
def outer0(func):
    def inner(*args, **kwargs):
        print("first decorate")
        result = func(*args, **kwargs)
        return result
    return inner

def outer1(func):
    def inner(*args, **kwargs):
        print("second decorate")
        result = func(*args, **kwargs)
        return result
    return inner

@outer0
@outer1
def index1(x, y):
    print(x, y)
    return True

index1(1, 2)