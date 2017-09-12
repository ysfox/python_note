#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 3.进度条.py
@time: 2017/8/21 下午3:25
@desc:
'''

import sys
import time

for i in range(1, 101):
    sys.stdout.write('\r')       # 每一次清空原行
    sys.stdout.write('%i%% %s' % (i, i*'#'))      # 第一个%防止转移
    sys.stdout.flush()           # 强制刷新到屏幕
    time.sleep(0.1)

sys.stdout.flush()
sys.stdout.write("\r")

