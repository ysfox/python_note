#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 7.带参数的装饰器.py
@time: 2017/8/29 下午2:15
@desc:
'''

# 1.带一个参数的装饰器
def outer(func):
    def inner(x):
        print("Start")
        result = func(x)
        print("End")
        return result
    return inner

@outer
def index(x):
    print(x)
    return True

result = index(1)
print(result)


# 2.带多个参数的装饰器
def outer(func):
    def inner(x, y):
        print("Start")
        result = func(x, y)
        print("End")
        return result
    return inner

@outer
def index(x, y):
    print(x, y)
    return True

index(1, 2)




# 3.带n个参数的装饰器
def outer(func):
    def inner(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return inner

@outer
def index1(x,):
    print(x)
    return True

@outer
def index2(x, y, z):
    print(x, y, z)
    return True

index1(33)
index2(44, 55, 66)





