#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 5.内置模块time.py
@time: 2017/8/21 下午4:00
@desc:
'''
import time

# 返回当前系统的时间
print(time.time())

# 计算机CPU执行时间
print(time.clock())

# UTC时间，结构化tuple
print(time.gmtime())

# 本地化时间，结构化tuple
print(time.localtime())

# print(time.strftime(format,tuple)) format格式 : %Y:%m:%d %H:%M:%S , tuple:结构化时间
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

# print(time.strptime(string time,format)) string time 对应的format格式 , 返回结构化时间
print(time.strptime("30 Nov 00", "%d %b %y"))

# print(time.ctime(时间戳))     # 时间戳 => string , Sat Nov 26 19:49:21 2016 ,当前系统时间
print(time.ctime(1503305112.4289632))

# print(time.mktime(tuple))    # 结构化时间tuple => 时间戳
print(time.mktime(time.gmtime()))

# print( time.localtime(时间戳) )     # 时间戳 float类型 => 结构化时间,tuple
print(time.localtime(1503305112.4289632))










