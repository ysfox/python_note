#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 4.类的三大特性之多态.py
@time: 2017/8/23 上午10:41
@desc:
'''

# 1.多态
# 多态是为了实现——接口重用！多态的作用:同一接口,多实现
# Pyhon不支持Java和C#这一类强类型语言中多态的写法，Python崇尚“鸭子类型”。
# 什么是填鸭式
# “鸭子类型”的语言是这么推断的：一只鸟走起来像鸭子、游起泳来像鸭子、叫起来也像鸭子，那它就可以被当做鸭子。
# 也就是说，它不关注对象的类型，而是关注对象具有的行为(方法)。
class F1:
    pass

class S1(F1):

    def show(self):
        print('S1.show')

class S2(F1):

    def show(self):
        print('S2.show')

# 鸭子类型
def Func(obj):
    print(obj.show())


s1_obj = S1()
Func(s1_obj) # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show

s2_obj = S2()
Func(s2_obj) # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show