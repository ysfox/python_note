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


t = threading.Thread(target=f1, args=(123, 111))
t.start()
# 默认情况下开启一个线程是和主线程一起并发任务，如果想串行执行线程可以使用join
# 也就是即开了线程，又想单个单个线程执行，则可以使用join，让主线程等待子线程
print("1111")           #主线程
# t.join()                #主线程会等待线程t执行完毕才执行主线程
t.join(1)               #主线程最多等待1秒，超过这个时间后主线程继续执行它自己的内容
print("2222")           #主线程