#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 11.装饰器的缺点.py
@time: 2017/8/29 下午4:22
@desc:
'''


# 1.装饰器的缺点
# 装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，比如函数的docstring、__name__、参数列表
# 不懂
from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return wrapper


@logged
def cal(x):
    return x + x * x


print(cal.__name__)  # cal