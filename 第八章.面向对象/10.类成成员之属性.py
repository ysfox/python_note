#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 10.类成成员之属性.py
@time: 2017/8/23 下午3:49
@desc:
'''


# 1、属性的两种定义方式
# 装饰器 即：在方法上应用装饰器
# 静态字段 即：在类中定义值为property对象的静态字段

# (1).装饰器方式：在类的普通方法上应用@property装饰器
# 装饰器方式又分为经典类和新式类
# 经典类，具有一种@property装饰器
class Goods:

    @property
    def price(self):
        return "wupeiqi"

obj = Goods()
print(obj.price)

# 新式类，具有三种@property装饰器
# 由于新式类中具有三种访问方式，我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deltter
    def price(self, value):
        del self.original_price

obj = Goods()
print(obj.price)         # 获取商品价格
obj.price = 200          # 修改商品原价
del obj.price            # 删除商品原价



# (2).静态字段方式:创建值为property对象的静态字段
class Foo:

    def get_bar(self):
        return 'wupeiqi'

    BAR = property(get_bar)

obj = Foo()
reuslt = obj.BAR        # 自动调用get_bar方法，并获取方法的返回值
print(reuslt)

# property的构造方法中有个四个参数
# 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
# 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
# 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
class Foo:

    def get_bar(self):
        return 'wupeiqi'

    # *必须两个参数
    def set_bar(self, value):
        return 'set value' + value

    def del_bar(self):
        return 'wupeiqi'

    BAR = property(get_bar, set_bar, del_bar, 'description...')

obj = Foo()

obj.BAR              # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "alex"     # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
del Foo.BAR          # 自动调用第三个参数中定义的方法：del_bar方法
obj.BAE.__doc__      # 自动获取第四个参数中设置的值：description...s