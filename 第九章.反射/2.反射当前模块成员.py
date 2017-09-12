#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 2.反射当前模块成员.py
@time: 2017/8/28 上午10:03
@desc:
'''

import sys


# 1.反射当前模块成员
def s1():
    print('s1')

def s2():
    print('s2')

this_module = sys.modules[__name__]
print(hasattr(this_module, 's1'))
print(hasattr(this_module, 's2'))
