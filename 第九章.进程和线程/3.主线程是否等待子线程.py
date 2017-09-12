#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF


import threading
import time

def f0():
    pass

def f1(a1, a2):
    print("线程启动前")
    time.sleep(2)
    print("线程启动后")
    f0()

# 默认主线程执行完毕会等待子线程，直到子线程执行完毕程序才结束
t = threading.Thread(target=f1, args=(123, 111))
# 如果想主线程执行完毕不等待子线程，可以设置守护线程为true
t.setDaemon(True)
t.start()

# 默认主线程执行完毕会等待子线程，直到子线程执行完毕程序才结束
t = threading.Thread(target=f1, args=(123, 111))
# 如果想主线程执行完毕不等待子线程，可以设置守护线程为true
t.setDaemon(True)
t.start()

# 默认主线程执行完毕会等待子线程，直到子线程执行完毕程序才结束
t = threading.Thread(target=f1, args=(123, 111))
# 如果想主线程执行完毕不等待子线程，可以设置守护线程为true
t.setDaemon(True)
t.start()

print("默认主线程执行完毕了会等待子线程")