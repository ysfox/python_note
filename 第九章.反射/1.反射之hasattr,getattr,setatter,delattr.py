#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.反射之hasattr,getattr,setatter,delattr.py
@time: 2017/8/25 下午5:33
@desc:
'''


# 1.反射概述


class People:
    country = 'China'

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)

p = People('alex', 'man')

# (1).hasattr(obj,name)   判断object中有没有一个name字符串对应的方法或属性
print(hasattr(p, 'name'))
print(hasattr(p, 'eat'))

# (2).getattr(obj,name,default)     检查obj._dict_中有没有name这个键值，有则不作任何处理，没有则报错
print(p.__dict__)
name = getattr(p, 'name')
print(name)
eat = getattr(p, 'eat')
eat()

# (3).setattr(obj, name, value)       相当于obj.name = value
setattr(p, 'name', 'sb')
name = getattr(p, 'name')
print(name)
setattr(p, 'run', lambda self: print(self.name+' is running'))
p.run(p)

# (4).delattr(obj, name)        相当于del obj.name
print(p.__dict__)
delattr(p, 'name')
print(p.__dict__)

