# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 18:02
# @Author  : Qin Yong
# @Email   : 327302008@qq.com
# @Site    : qinyong.site
# @File    : 3.socket实现简单FTP服务端.py
# @Software: PyCharm


import socket
import os
import hashlib

server = socket.socket()                # 获得socket实例
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8888))        # 绑定ip port
server.listen()                         # 开始监听

while True:
    print("等待新指令")
    # 接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    conn, addr = server.accept()
    print("新连接:", addr)

    data = conn.recv(1024)
    if not data:
        print("客户端已断开")
        break
    cmd, filename = data.decode().split()
    print(filename)
    if os.path.isfile(filename):
        f = open(filename, "rb")
        # 初始化MD5类
        m = hashlib.md5()
        file_size = os.stat(filename).st_size
        conn.send(str(file_size).encode())      # 发送文件大小
        conn.recv(1024)                         # 等待ack确认消息
        # 开始分段发送数据
        for line in f:
            # 更新需要计算md5的一行数据
            m.update(line)
            conn.send(line)
            print("file md5:", m.hexdigest())    # 查看一行的md5数据
            f.close()
            conn.send(m.hexdigest().encode())    # 发送最终的md5

        print("发送数据完毕")

server.close()

