#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.序列化之内置模块pickle.py
@time: 2017/8/21 下午5:14
@desc:
'''

import pickle

data = {'name': 'alex', 'age': 18}
# 1.pickle.dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)

# 2.pickle.loads 将只有python语言认识的字符串转换为原来的数据
print(pickle.loads(p_str))

# 3.pickle.dump 将数据通过特殊的形式转换为只有python语言认识的字符串,并写入文件
with open('ab.txt', 'wb')as f:
    pickle.dump(data, f)
    print("写入成功")

# 4.pickle.load 从文件中读取只有python语言认识的字符串，并转换为可大众识别的字符串
with open('ab.txt', 'rb')as f:
    data = pickle.load(f)
    print(data)
    print("读取成功")