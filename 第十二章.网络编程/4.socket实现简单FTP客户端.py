# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 20:46
# @Author  : Qin Yong
# @Email   : 327302008@qq.com
# @Site    : qinyong.site
# @File    : 4.socket实现简单FTP客户端.py
# @Software: PyCharm


import socket
import hashlib

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    cmd = input(">>:").strip()          # 命令类似：get text.txt
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        # 等待
        server_response = client.recv(1024)
        print("server response:", server_response)
        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename, "wb")
        m = hashlib.md5()

        while received_size < file_total_size:
            # 这里为了防治粘包，需要分段接收，总共的数据大小比已接收的数据大1024则还是按照1024大小接收
            if file_total_size - received_size > 1024:
                size = 1024
            else:       # 总共的数据大小比已接收的数据小1024则按照它们的差值计算
                size = file_total_size - received_size
                print("剩下没有接收的数据大小为：", size)

            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print("文件接收完毕,接收数据大小为%d,总文件大小为%d" % received_size, file_total_size)
            f.close()
    # 收完数据之后再次接收一下服务器返回的md5校验码
    serer_file_md5 = client.recv(1024)
    print("服务器文件返回的md5为:", serer_file_md5)
    print("客户端计算的md5为:", new_file_md5)

client.close()