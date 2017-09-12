#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 3.类的三大特性之继承.py
@time: 2017/8/23 上午10:11
@desc:
'''


# 1.继承
# 动物：吃、喝、拉、撒
class Animal:
    def eat(self):
        print("%s 吃 " % self.name)

    def drink(self):
        print("%s 喝 " % self.name)

    def shit(self):
        print("%s 拉 " % self.name)

    def pee(self):
        print("%s 撒 " % self.name)

# 猫：喵喵叫（猫继承动物的功能）
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.bread = '猫'

    def cry(self):
        print('喵喵叫')

 # 狗：汪汪叫（狗继承动物的功能）
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = '狗'

    def cry(self):
        print('汪汪叫')


# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()


# 2.多继承
# 经典类和新式类，从字面上可以看出一个老一个新，新的必然包含了跟多的功能，也是之后推荐的写法，从写法上区分的话，
# 如果当前类或者父类继承了object类，那么该类便是新式类，否则便是经典类。
# 经典继承
class D:

    def bar(self):
        print('D.bar')


class C(D):

    def bar(self):
        print('C.bar')


class B(D):

    def bar(self):
        print('B.bar')


class A(B, C):

    def bar(self):
        print('A.bar')

a = A()
# 执行bar方法时
# 经典类：首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有
# 则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
# 注意：在上述查找过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
# py2 经典类-> 深度优先  |  新式类 -> 广度优先
# py3 统一 广度优先 !
a.bar()


# 新式继承
class D(object):

    def bar(self):
        print('D.bar')


class C(D):

    def bar(self):
        print('C.bar')


class B(D):

    def bar(self):
        print('B.bar')


class A(B, C):

    def bar(self):
        print('A.bar')

a = A()
# 执行bar方法时
# 新式类：首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有
# 则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 注意：在上述查找过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
# py2 经典类-> 深度优先  |  新式类 -> 广度优先
# py3 统一 广度优先 !
a.bar()