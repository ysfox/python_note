#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 6.子类执行父类构造方法.py
@time: 2017/8/23 上午11:10
@desc:
'''


# 1.子类执行父类构造方法
# super(当前类,self).__init__()

# 方法一
class Annimal:
    def __init__(self):
        self.ty = 'annimal'

class Cat(Annimal):
    def __init__(self):
        self.n = 'cat'
        super(Cat, self).__init__()      # 新式类写法

c = Cat()
print(c.__dict__)                        # {'n': 'cat', 'ty': 'annimal'}


# 方法二(不推荐)
class Annimal:
    def __init__(self):
        self.ty = 'annimal'


class Cat(Annimal):
    def __init__(self):
        self.n = 'cat'
        Annimal.__init__(self)            # 经典类写法


c = Cat()
print(c.__dict__)                          # {'n': 'cat', 'ty': 'annimal'}




# 2.子类中调用父类方法
class Annimal(object):
    def sleep(self):
        print('Annimal Sleep')

class Cat(Annimal):
    def sleep(self):
        Annimal.sleep(self)   # 传递参数self
        print('Cat Sleep')

c = Cat()
c.sleep()
