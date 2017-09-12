#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF


#线程方法：
# start        激活线程，线程准备就绪，等待CPU调度
# setName      为线程设置名称
# getName      获取线程名称
# is_alive()   判断线程是否为激活状态
# isAlive()    判断线程是否为激活状态
# setDaemon    设置为后台线程或前台线程（默认：False）;通过一个布尔值设置线程是否为守护线程
#              必须在执行start()方法之后才可以使用
#              如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止
#              如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
# isDaemon()   判断是否为守护线程
# ident        获取线程的标识符,线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None
# join         逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
# run          线程被cpu调度后自动执行线程对象的run方法

import threading
import time

class Mythread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    #定义每个线程要运行的函数
    def run(self):
        print("线程%s执行开始" % str(self.num))
        time.sleep(2)
        print("线程%s执行结束" % str(self.num))

if __name__ == "__main__":
    t1 = Mythread(1)
    t2 = Mythread(2)
    t1.start()
    t2.start()
    print("默认主线程执行完毕了会等待子线程")