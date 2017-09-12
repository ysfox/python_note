#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 13.强制访问私有字段.py
@time: 2017/8/24 上午11:01
@desc:
'''


# 1.强制访问私有字段
# 非要访问私有属性的话，可以通过 对象._类__属性名
class C:
    def __init__(self):
        self.__foo = "私有普通字段"
    def func(self):
        print(self.__foo)         # 类内部访问
class D(C):
    def show(self):
        print(self.__foo)         # 派生类中访问

obj = C()
obj_son = D()

# 私有字段不能直接访问，只能在类内部访问
# print(obj.__foo)          #错误，不能通过对象访问
# obj_son.show()            #错误，不能通过派生类访问
obj.func()                  #正确，只能在类内部访问
# 如果要强制访问,可以对象._类__属性名方法
print(obj._C__foo)



# 方法、属性的访问于上述方式相似，即：私有成员只能在类内部使用