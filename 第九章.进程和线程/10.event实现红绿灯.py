#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:CF

import threading
import time
import random

def light():
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--绿灯亮--\033[0m')
            if not event.isSet:
                event.set()
        elif count < 13:
            print('\033[43;1m--黄灯亮--\033[0m')
        elif count < 20:
            print('\033[41;1m--红灯亮--\033[0m')
        else:
            count = 0
        time.sleep(1)
        count += 1


if __name__ == "__main__":
    event = threading.Event
    light_thread = threading.Thread(target=light())
    light_thread.start()

