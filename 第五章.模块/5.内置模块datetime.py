#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 6.内置模块datetime.py
@time: 2017/8/21 下午4:57
@desc:
'''

import datetime
import time
#  #返回 2016-11-26 20:04:32.586288
print(datetime.datetime.now())

# 时间戳直接转成日期格式 2016-11-26
print(datetime.datetime.fromtimestamp(time.time()))

# 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(3))

# 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(-3))

# 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(hours=3))

# 当前时间+1周
print(datetime.datetime.now() + datetime.timedelta(weeks=1))

#时间替换
c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))

# datetime <=> string
# datetime -> string
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# string -> datetime
print(datetime.datetime.strptime("2016-11-26 20:20:20", "%Y-%m-%d %H:%M:%S"))


# datetime <=> date
# datetime -> date
print(datetime.datetime.now().date())
# date -> datetime
today = datetime.date.today()
datetime = datetime.datetime.combine(today, datetime.time())
print(datetime)