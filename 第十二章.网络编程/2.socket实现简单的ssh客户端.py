# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 14:28
# @Author  : Qin Yong
# @Email   : 327302008@qq.com
# @Site    : qinyong.site
# @File    : 2.socket实现简单的ssh客户端.py
# @Software: PyCharm


import socket

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    # 发送ssh的指令
    client.send(cmd.encode("utf-8"))
    # 接收命令执行结果的长度，这里会阻塞等待服务端返回命令执行结果的长度
    cmd_res_size = client.recv(1024)
    print("命令执行结果返回长度为:", cmd_res_size)
    # ack响应，解决粘包ack回应
    client.send("服务端我收到数据大小了你可以数据了".encode("utf-8"))
    received_size = 0
    received_data = b''
    # 开始接收命令执行后的响应数据
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)          # 计算当前获取到的数据大小
        received_data += data
    else:
        # 接收完毕
        print("返回数据总大小为:", received_size)
        print(received_data.decode())

client.close()