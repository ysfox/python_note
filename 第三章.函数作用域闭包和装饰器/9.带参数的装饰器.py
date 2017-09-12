#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 9.带参数的装饰器.py
@time: 2017/8/29 下午3:09
@desc:
'''

import time

# 带参数的装饰器
def time_logger(flag=0):
    def show_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('spend %s time' % (end_time - start_time))
            if flag:
                print('将操作时间记录到日志中去')
        return wrapper
    return show_time

@time_logger(3)
def add(*args, **kwargs):
    time.sleep(1)
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(2, 7, 5)