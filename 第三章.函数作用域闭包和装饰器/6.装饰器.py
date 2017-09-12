#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 6.装饰器.py
@time: 2017/8/29 下午2:03
@desc:
'''

# 1.装饰器
# 写代码要遵循开发封闭原则,虽然在这个原则是用的面向对象开发,但是也适用于函数式编程
# 简单来说它规定已经实现的功能代码不允许被修改但可以被扩展,即
# 封闭:已实现的功能代码块
# 开放:对扩展开发

def outer(func):
    def inner():
        print("Start")
        result = func()
        print("End")
        return result
    return inner

@outer              #index = outer(index)
def index():
    print("hello sb")
    return True

result = index()