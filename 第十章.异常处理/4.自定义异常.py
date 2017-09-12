#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 4.自定义异常.py
@time: 2017/8/25 上午11:44
@desc:
'''


# 1.自定义异常
class SbException(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message

input_str = input("请不要输入含有傻逼的文字:")
try:
    if "傻逼" in input_str:
        raise SbException("请不要输入含傻逼字样的内容...")
    else:
        print("输入正确")
except SbException as e:
    print(e)