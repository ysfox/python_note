#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF


# 1.普通参数函数
def func1(name):
    print(name)

func1("傻逼")



# 2.带默认参数的函数
def func2(name, age = 100):
    print("%s的年纪是%d"% (name, age))

func2("王八蛋")



# 3.可变参数一
def func3(*args):
    print(args, type(args))

# 第一种调用方法
func3(77, 88, 99)
# 第二种调用方法
li = [11, 22, 33, 44, 55, 66]
func3(*li)                      #([11, 22, 33, 44, 55, 66],) <class 'tuple'>
# 注意传递的参数，注意此处!元组第一个元素为列表
func3(li)



# 4.可变参数二
def func4(**kwargs):
    print(kwargs, type(kwargs))

# 第一种调用方法
func4(name="sb", age=100)
# 第二种调用方式
dic = {"name": "sb", "age": 100}
func4(**dic)



# 5.混合方式
def func5(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

func5(11, 22, 33, 44, name="123", age=321)


# 函数作为参数传递
def fn1():
    print("fun1方法执行")

def fn2(fn):
    fn()
    print("fun2方法执行")

fn2(fn1)



