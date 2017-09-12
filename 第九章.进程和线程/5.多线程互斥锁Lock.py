#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

import threading
import time


# 1.锁的作用
# 我们使用线程对数据进行操作的时候，如果多个线程同时修改某个数据
# 可能会出现不可预料的结果，为了保证数据的准确性，引入了锁的概念。

gl_num = 0
# 创建一把线程数
lock = threading.Lock()
# 线程执行函数，我们可以将锁注释掉，看看结果
def fun():
    lock.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    lock.release()

for i in range(10):
    t = threading.Thread(target=fun)
    t.start()

print("主线程执行完毕默认等待子线程执行...")


# 2.RLock和Lock的区别
# RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
# 如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。
# 比如说递归锁

