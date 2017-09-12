#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF


# 定时器，指定n秒后执行某操作
# start 开启定时线程
# cancel 停止定时线程

from threading import Timer

def fun():
    print("hello world")

if __name__ == "__main__":
    t = Timer(3, fun)       #3秒后执行fun函数
    t.start()