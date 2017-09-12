#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 5.文件处理之自动管理上下文.py
@time: 2017/8/25 下午4:41
@desc:
'''

# 1.自动管理上下文
# 为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open('log.log', 'r') as f:
    print(f.read())

# 2.多文件管理上下文
# with又支持同时对多个文件的上下文进行管理
with open('log1.log', 'r') as f1,open('log2.log', 'a') as f2:
    # readlines 同时会把换行符读出来,需要用strip()去掉!
    for line in f1.readlines():
        data = line.strip()
        f2.write('\n' + data)


