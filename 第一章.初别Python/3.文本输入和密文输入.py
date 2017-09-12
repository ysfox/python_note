#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "QinYong"

import getpass


name = input("请他妈输入你的大名:")
print("name:", name)

# 在pycharm中无效果？？
pwd = getpass.getpass("大爷输入你的密码:")
print("password", pwd)