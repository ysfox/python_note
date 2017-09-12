#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 2.异常的种类.py
@time: 2017/8/25 上午11:17
@desc:
'''


# 1.常用异常的种类
# python中的异常种类非常多，每个异常专门用于处理某一项异常！！！
# AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError 语法错误
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的

# 例子1,IndexError
li = ['alex0', 'alex1']
try:
    print(li[10])
except IndexError as e:
    print("异常出现:", e)


# 例子2，KeyError
dic = {'key1':"value1"}
try:
    print(dic["key2"])
except KeyError as e:
    print("异常出现:", e)


# 例子3，ValueError
value = "hello"
try:
    int(value)
except ValueError as e:
    print("异常出现:", e)

