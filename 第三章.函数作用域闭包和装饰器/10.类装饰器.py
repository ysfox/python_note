#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 10.类装饰器.py
@time: 2017/8/29 下午3:52
@desc:
'''

import time
# 1.类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self._func()
        end_time = time.time()
        print('spend %s' % (end_time - start_time))

@Foo        #bar = Foo(bar)
def bar():
    print('bar')
    time.sleep(2)

bar()