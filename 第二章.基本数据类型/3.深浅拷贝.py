#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:"Qin Yong"

import copy

# 1.对于数字和字符串而言深浅拷贝无意义,因为它们永远指向一个固定的内存地址
a = 123
b = 'sb'
# 浅拷贝
aa = copy.copy(a)
bb = copy.copy(b)
# 深拷贝
aaa = copy.deepcopy(a)
bbb = copy.deepcopy(b)
print(id(a), id(aa), id(aaa))  # 三个相同
print(id(b), id(bb), id(bbb))  # 三个相同

# 2.对于字典、元祖、列表而言进行赋值，深浅拷贝的内存地址是不同的
# 赋值
n1 = {"k1": "wu", "k2": "123", "k3": ["alex", "456"]}
n2 = n1
print(id(n1), id(n2))       #4300911432 4300911432

# 浅拷贝
n3 = copy.copy(n1)
print(id(n1), id(n3))       #4300911432 4301797512

# 深拷贝
n4 = copy.deepcopy(n1)
print(id(n1), id(n4))       #4300911432 4301398856