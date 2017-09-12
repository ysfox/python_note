#!/usr/bin/env python
# encoding: utf-8
'''
@author: Qin Yong
@license: (C) Copyright 2013-2017,DuoMeng Technology Co.,Ltd
@contact: 327302008@qq.com
@file: 3.文件处理之三种模式.py
@time: 2017/8/25 下午3:43
@desc:
'''


# 1.文件处理模式
# 文件句柄 = open('文件路径', '模式','编码')
# (1).普通模式：
# r，只读模式【默认】
# w，只写模式【不可读；不存在则创建；存在则清空内容!】
# x，只写模式【不可读；不存在则创建，存在则报错】
# a，追加模式【可读；不存在则创建；存在则只追加内容!】

f = open('log.log', 'r', encoding='utf-8')
data = f.read()
print(data)



# (2).+模式：
# "+" 表示可以同时读写某个文件
# r+， 读写【可读，可写】指针为0
# w+， 写读【可读，可写】
# x+， 写读【可读，可写】
# a+， 写读【可读，可写】打开同时指针移动到 最后
# 注意：r+中指针为0，当f.write('abc')则会从开始写，如果此时有内容会覆盖掉
#      r+中指针为0，当f.read()执行后指针去到末尾，此时执行f.write()则从末尾开始写

f = open('log.log', 'r+', encoding='utf-8')
print(f.read())         #abcdefg
print(f.tell())         #7      #当前指针到末尾了
f.close()

f = open('log.log', 'r+', encoding='utf-8')
f.write('123')
print(f.tell())         #指针到到3的位置了
print(f.read())         #结果为defg
f.close()



# (3).字节模式
# 文件句柄 = open('文件路径', '模式')
# rb 或 r+b
# wb 或 w+b
# xb 或 w+b
# ab 或 a+b
# 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型
# 注: windows上,写操作默认为GBK编码,Linux为utf-8,需要注明编码类型防止错误
f = open('blob.log', 'w+b')
byte_list = bytes('傻逼', encoding='utf-8')
f.write(byte_list)
f.close()

f = open('blob.log', 'r+b')
data_list = f.read()
print(data_list)
print(str(data_list, encoding='utf-8'))
f.close()