#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 4.作用域.py
@time: 2017/8/28 上午10:41
@desc:
'''

# 1.作用域
# (1).作用域分为LEGB
# L：local，局部作用域,即函数中定义的变量
# E：enclosing,嵌套的父级函数的局部作用域,即包含此函数的上级函数的局部作用域但不是全局的
# G：globa,全局变量，就是模块级别定义的变量
# B：built-in,系统固定模块里面的变量,比如int,bytearray等
# 优先级顺序依次是:作用域局部 > 外层作用域 > 当前模块中的全局 > python内置作用域,也就是LEGB。

x = int(2.9)           #int buitt-in
g_count = 0            #global
def outer():
    o_count = 1        #enclosing
    def inner():
        i_count = 2    #local
        print(o_count)
    inner()
outer()


# (2).注意:在Python中，只有模块(module),(class)以及函数(def、lambda)才会引入新的作用域，
# 其它的代码块(如if、try、for等)是不会引入新的作用域的
a_string = "This is a global variable"
def foo():
    print(locals())             #函数foo有自己独立的命名空间,虽然暂时命名空间里面什么都还没有
print(globals())                #内置的函数globals返回一个包含所有python解释器知道的变量名称的字典
foo()



# (3).global关键字
# 当修改的变量是在全局作用域（global作用域）上的，就要使用global先声明一下
count = 10
def outer():
    global count
    print(count)        #10
    count = 100
    print(count)        #100
outer()


# (4).nonlocal关键字
# 不能嵌套作用域上，当要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量怎么办呢，这时就需要nonlocal关键字了
def outer():
    count = 10
    def inner():
        nonlocal count  #
        count = 20
        print(count)    #20
    inner()
    print(count)        #20
outer()



