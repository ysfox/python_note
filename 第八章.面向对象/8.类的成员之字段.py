#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 8.类的成员之字段.py
@time: 2017/8/23 上午11:48
@desc:
'''


# 1.字段
# 字段包括：普通字段和静态字段，普通字段属于对象，静态字段属于类
# 静态字段在内存中只保存一份
# 普通字段在每个对象中都要保存一份
# 应用场景： 通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段
class Province:
    # 静态字段
    country = '中国'
    def __init__(self, name):
        # 普通字段
        self.name = name

# 普通字段需要通过对象来访问
obj = Province('河北省')
print(obj.name)
# 静态字段通过类访问
print(Province.country)






# 3.属性
# Python中的属性其实是普通方法的变种
# 1、属性的基本使用
class Foo:
    def func(self):
        pass

    # 定义属性时，在普通方法的基础上添加 @property 装饰器；
    @property
    def prop(self):     #定义时，属性仅有一个self参数
        pass

foo_obj = Foo()
foo_obj.func()
#调用时无需括号
print(foo_obj.prop)






# 3、属性的功能
# Python的属性的功能是：属性内部进行一系列的逻辑计算，最终将计算结果返回。
# 例子：数据库请求分页功能
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(1)
# 就是起始值，即：m
print(p.start)
# 就是结束值，即：n
print(p.end)
