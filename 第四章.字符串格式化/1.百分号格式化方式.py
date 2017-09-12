#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 1.百分号格式化方式.py
@time: 2017/8/21 上午11:54
@desc:
'''

# 1.百分号格式化方式
# %[(name)][flags][width].[precision]typecode
# name表示指定的key
# flags可选宽度width占有的宽度
# .precision可选表示小数点保留多少位
# typecode必须参数：类型如下
# s,获取对象的__str__方法的返回值
# r,获取对象的__repr__方法的返回值
# c,将数字转换为对应的ascii码或将匹配字符
# o,将整数转换成八进制
# x,将整数转换为十六进制
# d,将整数，浮点数转换成十进制
# f,将整数，浮点数转换成浮点数表示
# %,格式化%号

class Foo:
    def __repr__(self):
        return "hello wrold"

    def __str__(self):
        return "hello python"

print("Foo's reps is '%r'" % Foo())
print("Foo's str is '%s'" % Foo())
print("100's ascii is %c" % 100)
print("you selected char is %c" % 'A')
print("8's oct is %o" % 8)
print("16's hex is %x" % 16)
print("100.123's int is %d" % 100.123)
print("100's float number is %f" % 100)
print("100's float number is %.2f" % 100)
print("I am %(name)s and age is %(age)d" % {"name": "wbd", "age": 23})



# 2.Format方式
# [[fill]align][sign][#][0][width][,][.precision][type]
# fill,可选参数，空白处填充的字符
# align,可选参数，对齐方式，需要配合width使用，<左对齐，>右对齐，=内容右对齐符号左对齐中间用填充字符，^内容居中
# sign,可选参数，有无符号，+整数加正负数加负，-正号不变负号加负，空格正号加空格负号加负
# #，可选参数，对于二进制，八进制，十六进制，如果加上#则会显示前缀0b/0o/0x
# width,可选参数，格式化位所占宽度
# ,,可选参数，为数字添加分隔符,如：1,000,000
# .precision,可选参数，小数位保留精度
# type,可选参数，表示格式化类型:
    #s,格式化字符串类型数据
    #b,十进制整数转二进制
    #c,将十进制整数转换为对应的unicode字符
    #d,格式化为十进制整数
    #o,将十进制整数转成八进制
    #x,将十进制整数转换为十六机制(小写x)
    #X,将十进制整数转换为十六机制(大写X)
    #e,将浮点数转为科学计数法(小写e)表示
    #E,将浮点数转为科学计数法(大写E)表示
    #f,转换为浮点数表示，默认保留6位
    #F,转换为浮点数表示，默认保留6位
    #g,自动在e和f中切换
    #G,自动在E和F中切换
    #%,格式化%
print("I am {}, age is {}".format("LiLei", 100))
print("I am {}, age is {}".format(*["Tom", 100]))
print("I am {0}, age is {1}, my name is {0}".format("LaoWang", 110))
print("I am {0}, age is {1}, my name is {0}".format(*["LaoLi", 1000]))
print("My name is {name}, age is {age}".format(name="zhangsan",age=18))
print("My name is {name}, age is {age}".format(**{"name": "lisi", "age": 100}))
print("select number is {0[0]}, want number is {1[0]}".format([1, 2, 3], [33, 44, 55]))
print("my name is{:s},i am {:d} year old,i have {:f} money".format("Lily", 18, 10001.2))
print("my name is{:s},i am {:d} year old,i have {:f} money".format(*["Lily", 18, 10001.2]))
print("my name is{name:s},i am {age:d} year old,i have {money:f} money".format(name="Lily", age=100, money=12222.1))
print("my name is{name:s},i am {age:d} year old,i have {money:f} money".format(**{"name": "Lily", "age": 100, "money": 122.222}))
print("numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2))
print("numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15))
print("numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15))







