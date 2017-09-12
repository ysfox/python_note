# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 21:47
# @Author  : Qin Yong
# @Email   : 327302008@qq.com
# @Site    : qinyong.site
# @File    : 6.测试socketServer的客户端.py
# @Software: PyCharm


import socket

client = socket.socket()
client.connect_ex(('localhost', 9999))
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print("接收到的数据为：", data.decode())

client.close()