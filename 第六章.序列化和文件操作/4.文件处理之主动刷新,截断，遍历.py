#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 4.文件处理之主动刷新,截断，遍历.py
@time: 2017/8/25 下午4:30
@desc:
'''

# 1.主动刷新
f = open('log.log', 'a+', encoding='utf-8')
f.write('123')
f.flush()
input(">>>输入中断，此时已经将内容主动刷新到文件中:")
f.close()


# 2.截断
f = open('log.log', 'r+', encoding='utf-8')
# 需要写操作,从指针为3处截断, 不要后面的内容,这种输出方式会把文本中的换行符也输出~ 可以用 i.strip() 　　去除换行符!!
print(f.truncate(3))
print(f.read())
f.close()


# 3.遍历每行内容
# 这种输出方式会把文本中的换行符也输出~ 可以用 i.strip()去除换行符!!
f = open('log.log', 'r', encoding='utf-8')
for i in f:
    print(i.strip())
f.close()

