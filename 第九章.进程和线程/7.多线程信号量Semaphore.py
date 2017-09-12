#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

# Semaphore(信号量)
# 互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据
# 比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。


import threading
import time

def fun(n):
    semaphore.acquire()
    print("run the thread: %s" % n)
    print("current num is %d \n" % num)
    global num
    num += 1
    time.sleep(1)
    semaphore.release()
    pass

if __name__ == "__main__":
    num = 0
    semaphore = threading.BoundedSemaphore(5)       #最多允许5个线程同时运行
    for i in range(10):
        t = threading.Thread(target=fun, args=(i,))
        t.start()


while threading.active_count() != 1:
    pass #print threading.active_count()
else:
    print('----all threads done---')
    print(num)