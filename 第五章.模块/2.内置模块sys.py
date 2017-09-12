#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 2.内置模块sys.py
@time: 2017/8/21 下午3:07
@desc:
'''
import sys

# 1.sys用于提供对Python解释器相关的操作


#sys.argv命令行参数List，第一个元素是程序本身路径
print(sys.argv)
#sys.exit(n)退出程序，正常退出时exit(0)
# print(sys.exit("退出了应用"))
#sys.version获取Python解释程序的版本信息
print(sys.version)
#sys.path返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)
#sys.platform返回操作系统平台名称, 如win32
print(sys.platform)
#sys.stdin输入相关
print(sys.stdin)
#sys.stdout输出相关
print(sys.stdout)
# 强制刷新到屏幕
sys.stdout.flush()
# 每一次清空原行
sys.stdout.write("\r")
# 输出后,没有换行
sys.stdout.write("hello")
# 自动换行
print("hello")
