#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 3.随机验证码.py
@time: 2017/8/21 上午11:35
@desc:
'''

import random

validate_code = ''
for i in range(4):
    n = random.randrange(0, 4)
    if n == 1 or n == 3:
        random_num = random.randrange(0, 10)
        validate_code += str(random_num)
    else:
        random_num = random.randrange(65, 91)
        validate_code += chr(random_num)

print(validate_code)