#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 5.多继承易错点.py
@time: 2017/8/23 上午10:58
@desc:
'''


class A:
    def bar(self):
        print('BAR')
        self.f1()


class B(A):
    def f1(self):
        print('B')


class C:
    def f1(self):
        print('C')


class D(C, B):
    pass


d1 = D()
# 上述代码,执行过程:现在class D中寻找bar()方法,没有 -> 去父类class C中查找,还是没有 -> 再到class B -> class A中找到bar()方法.并执行,
# 此时代码中的self.f1()中的self代表为d1 -> 又重头开始在class D中寻找f1()方法 ...
# 需要注意: self 执行者,  在我们查看源码过程中, 遇到self.xxxx() 应该从头开始查找!
d1.bar()


# 结果
# Bar
# C