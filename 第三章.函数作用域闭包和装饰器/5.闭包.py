#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 5.闭包.py
@time: 2017/8/28 下午5:40
@desc:
'''

# 5.闭包
# 嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间。
def outer():
    x = 1
    def inner():
        print(x)
    return inner
foo = outer()       #每次函数outer被调用的时候，函数inner都会被重新定义。
foo()
print(foo.__closure__)
