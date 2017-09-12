#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:"Qin Yong"

# 3.其它内容
# (1).for循环
list = [11, 22, 33, 44]
for item in list:
    print(item)

# (2).enumerate为可迭代对象天添加序列
for k, v in enumerate(list, 1):
    print(k, v)

# (3).range和xrange指定范围生成指定数字
print(range(1, 10))
print(range(1, 10, 2))
print(range(30, 0, -2))
