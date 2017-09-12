#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "QinYong"


import code

name = "李璐"
# 打印字符串
print(name)

# 获取字符的长度
print(len(name))

# 将中文字符转换成二进制
for i in name:
    print(i)               # 输入单个文字
    byte_list = bytes(i, encoding='utf8')
    print(byte_list)       # 在utf8中，一个汉字有3个字节
    for b in byte_list:
        print(b, bin(b))   # 将unicode码转换成二进制
