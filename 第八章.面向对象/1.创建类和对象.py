#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.创建类和对象.py
@time: 2017/8/23 上午9:55
@desc:
'''

# python比较灵活即支持面向对象编程也支持函数式编程
# 1.创建类和对象
class Foo1:
    # 这里构造方法中有self表示实例化时会自动把这个实例本身通过self传递进去
    def __init__(self, name):
        self.name = name

    # 类中的函数第一个参数必须是self
    def Bar(self):
        print("bar")

    def Hello(self, name):
        print('I am %s' % name)

# 根据类Foo创建对象obj
obj = Foo1("SB")
obj.Bar()            # 执行Bar方法
obj.Hello('wupeiqi') # 执行Hello方法　




