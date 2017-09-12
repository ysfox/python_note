#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 3.反射的作用.py
@time: 2017/8/28 上午10:06
@desc:
'''

# 1.反射的作用
# (1).即插即用,热插拔
class FtpClient:       # 仅定义，不实现具体方法,具体由子类去实现接口
    def __init__(self, addr):
        print('正在连接服务器[%s]' % addr)
        self.addr = addr

# 这个需要由子类去实现具体的接口
f1=FtpClient('192.168.1.1')
if hasattr(f1, 'get'):
    func_get = getattr(f1, 'get')
    func_get()
else:
    print('not exist')


# (2).动态导入模块，通过字符串名称导入模块
import importlib
t = importlib.import_module('time')
print(t.time())