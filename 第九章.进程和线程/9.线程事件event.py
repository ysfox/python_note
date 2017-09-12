#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

import threading

# threading.Event
# Event是线程间通信最间的机制之一：一个线程发送一个event信号，其他的线程则等待这个信号。用于主线程控制其他线程的执行。
# Events管理一个flag，这个flag可以使用set()设置成True或者使用clear()重置为False，wait()则用于阻塞，它相当于把flag为True之前。flag默认为False。
# 当线程执行的时候，如果flag为False，则线程会阻塞，当flag为True的时候，线程不会阻塞。它提供了本地和远程的并发性。
# Event.wait([timeout]) ： 堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
# Event.set() ：将标识位设为Ture
# Event.clear() ： 将标识伴设为False。
# Event.isSet() ：判断标识位是否为Ture。


def fun(event):
    print("线程%s执行开启" % threading.current_thread().getName())
    #默认wait相当于红灯，所有的线程都阻塞在这里
    event.wait()
    print("线程%s执行结束" % threading.current_thread().getName())

event = threading.Event()
if __name__ == "__main__":
    for i in range(10):
        t = threading.Thread(target=fun, args=(event,))
        t.start()

input_value = input("是否是绿灯:")
if input_value == 'true':
    # set相当于开启绿灯，clear相当于开启绿灯
    event.set()

