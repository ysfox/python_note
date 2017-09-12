#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 3.多异常处理.py
@time: 2017/8/25 上午11:26
@desc:
'''

# 1.多异常处理
# 如果在处理异常过程中，未捕获到的异常，程序将会直接报错
# 例如下面代码出现的异常是ValueError,即传入一个调用者不期望的值
# 但是我们捕获的异常却是下表越界异常，所以程序任然报错误
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print("异常出现:", e)

# 所以写程序时需要考虑到try代码块中可能出现的任意异常，可以这样写：
try:
    int(s1)
except IndexError as e:
    print("索引异常出现:", e)
except KeyError as e:
    print("不存在的键异常出现:", e)
except ValueError as e:
    print("不期望的值异常出现:", e)

# 另外我们也可以用万能异常Exception捕获任意异常,但是不建议这样做，理由是不方便查看具体的异常情况
num = input("num:")
try:
    if not num.isdigit():
        raise Exception("请输入数字...")
    else:
        print("输入正确")
except Exception as e:
    print(e)
