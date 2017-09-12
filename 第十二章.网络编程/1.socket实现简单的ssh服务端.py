# -*- coding: utf-8 -*-
# @Time    : 2017/9/7 10:30
# @Author  : Qin Yong
# @Email   : 327302008@qq.com
# @Site    : qinyong.site
# @File    : 1.socket实现简单的ssh服务端.py
# @Software: PyCharm


import socket
import os

server = socket.socket()            # 获得socket实例
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 9999))    # 绑定ip port
server.listen()                     # 开始监听
while True:
    # 接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    conn, addr = server.accept()
    print("新连接地址为：", addr)
    while True:
        cmd = conn.recv(1024)
        if not cmd:
            print("客户端已经断开")
            break                                       # 这里断开就会再次回到第一次外层的loop
        print("执行指令:", cmd)
        # py3里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
        cmd_res = os.popen(cmd.decode()).read()         # 执行指令的结果也是字符串
        if len(cmd_res) == 0:
            cmd_res = "此命令没有输出内容"
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))       # 先将大小发送给客户端
        # 注意这个地方需要解决粘包问题,解决粘包的关键就是等待客户端收到数据并响应
        client_ack = conn.recv(1024)
        print(client_ack.decode())
        # 客户端有响应之后将命令执行结果返给客户端
        conn.send(cmd_res.encode("utf-8"))
        print("发送数据完毕")


server.close()

