#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 2.序列化之内置模块json.py
@time: 2017/8/21 下午5:30
@desc:
'''

import json

data = {'name': 'alex', 'age': 18}
# 1.json.dumps  将python基本数据类型  => 将字符串
# 将数据通过特殊的形式转换为所有语言都认识的字符串
j_str = json.dumps(data)
print(j_str)

# 2.json.loads  将字符串 => python基本数据类型
# 用于将字典,列表,元组形式的字符串 装换成 字典,列表,元组
# 注意: 如果 字典内的元素 是字符串要用双引号!
print(json.loads(j_str))

# 3.json.dump 将数据通过特殊的形式转换为所有语言都认识的字符串,并写入文件
with open('cd.txt', 'w')as f:
    json.dump(data, f)

# 简写
json.dump({'k1': 123,'k2': 'v2' }, open('db.txt', 'w'))

# 4.json.load 从文件中读取字符串转换成数据
with open('cd.txt', 'r')as f:
    data = json.load(f)
    print(data)

# 简写
print(json.load(open('cd.txt', 'r')))



