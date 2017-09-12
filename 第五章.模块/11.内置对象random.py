#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

import random

print(random.random())  # (0,1)之间的浮点数

print(random.randint(1, 3))  # [1,3]区间的随机整数值

print(random.randrange(1, 3))  # [1,3)区间的任意值

print(random.choice([1, '23', [4, 5]]))  #从非空序列中随机选择一个元素

print(random.sample([1, '23', [4, 5]], 2))  #从序列或者集合中选择唯一的随机元素

"Get a random number in the range [a, b) or [a, b] depending on rounding."
print(random.uniform(1, 3))   #获取区间随机浮点数值