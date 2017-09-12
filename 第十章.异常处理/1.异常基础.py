#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.异常基础.py
@time: 2017/8/25 上午11:11
@desc:
'''

# 1、异常基础
# (1).异常的基本结构一
try:
    # 主代码块
    pass
except Exception as ex:
    # 异常时，执行该块
    pass

# 例子：将用户输入的两格数字相除
while True:
    num1 = input("num1:")
    num2 = input("num2:")
    try:
        result = int(num1)/int(num2)
    except Exception as e:
        print("出现异常:" ,e)


# (2).异常的基本结构二
try:
    #主代码块
    pass
except KeyError as e:
    #异常时，执行该快
    pass
else:
    #主代码块执行完，执行该快
    pass
finally:
    #无论异常与否，最终执行该快
    pass


# 2.主动触发异常
num = input("num:")
try:
    if not isdigit(num):
        raise Exception("请输入数字...")
except Exception as e:
    print(e)
