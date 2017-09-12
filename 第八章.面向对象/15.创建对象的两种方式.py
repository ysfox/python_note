#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 15.创建对象的两种方式.py
@time: 2017/8/24 下午4:16
@desc:
'''


# 1.创建对象的两种方式
class Foo(object):
    def func(self):
        print("hello world")

# obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，Foo类本身也是一个对象，因为在Python中一切事物都是对象。
# obj对象是Foo类的一个实例，Foo类对象是 type 类的一个实例，即：Foo类对象 是通过type类的构造方法创建。
obj = Foo()
print(type(obj))  # 输出：<class '__main__.Foo'>     表示，obj 对象由Foo类创建
print(type(Foo))  # 输出：<type 'type'>              表示，Foo类对象由 type 类创建


# 那么，创建类就可以有两种方式：
# (1).普通方式
class Clazz1(object):
    def func(self):
        print("hello world")

# (2).特殊方式(type类的构造函数)
def func(self):
    print("hello world")
# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员
Clazz2 = type('Clazz2', (object,), {'func': func})



# 2.type类中如何实现的创建类 __new__ 和 __metaclass__
# 类默认是由 type 类实例化产生，type类中如何实现的创建类？类又是如何创建对象？
# 答：类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，
# 所以我们可以为 __metaclass__ 设置一个type类的派生类，从而查看 类 创建的过程。
class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj)

class Foo(object):
    __metaclass__ = MyType
    def __init__(self, name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象S
obj = Foo()