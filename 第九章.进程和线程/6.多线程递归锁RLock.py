#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

# RLock（递归锁）
# 说白了就是在一个大锁中还要再包含子锁
import threading
import time

def run1():
    print("线程%s执行run1方法" % threading.current_thread().getName())
    rlock.acquire()
    global num1
    num1 += 1
    rlock.release()
    return num1


def run2():
    print("线程%s执行run2方法" % threading.current_thread().getName())
    rlock.acquire()
    global num2
    num2 += 1
    rlock.release()
    return num2

def run3():
    rlock.acquire()
    result1 = run1()
    result2 = run2()
    rlock.release()
    print("num1=%d,num2=%d" % (result1, result2))

if __name__ == "__main__":
    num1, num2 = 0, 0
    rlock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=run3())
        t.start()

while threading.active_count() != 1:
    print("----------------%d" % threading.active_count())
else:
    print('----all threads done---')
    print(num1, num2)