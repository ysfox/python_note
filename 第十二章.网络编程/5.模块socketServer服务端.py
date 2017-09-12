# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 20:46
# @Author  : Qin Yong
# @Email   : 327302008@qq.com
# @Site    : qinyong.site
# @File    : 5.模块socketServer服务端.py
# @Software: PyCharm

# 1.SocketServer
# 四种类
# class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
# class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
# class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
# class socketserver.UnixDatagramServer(server_address, RequestHandlerClass,bind_and_activate=True)
# 继承关系
# +------------+
# | BaseServer |
# +------------+
#       |
#       v
# +-----------+        +------------------+
# | TCPServer |------->| UnixStreamServer |
# +-----------+        +------------------+
#       |
#       v
# +-----------+        +--------------------+
# | UDPServer |------->| UnixDatagramServer |
# +-----------+        +--------------------+

# class socketserver.BaseServer(server_address, RequestHandlerClass) 主要有以下方法
# fileno()  文件描述符
# handle_request() 处理单个请求
# serve_forever(poll_interval=0.5)  处理请求信号并每0.5秒检查是否有shutdown的信号
# service_actions() 被serve_forever循环调用此方法
# shutdown() 停止处理请求
# server_close()    清理服务
# address_family    sockect的协议
# RequestHandlerClass   socket的请求处理类
# server_address        socket的地址
# socket                socket的的socket独享
# allow_reuse_address   socket是否允许重复地址
# socket_type           socket使用的协议类型
# timeout               socket超时时间，在handle_requet中会用
# finish_request()      socket请求结束后的处理方法
# get_request()         获取socket的
# handle_error(request, client_address)       错误处理
# handle_timeout()                            处理超时
# process_request(request, client_address)    进程请求
# server_activate()                           服务是否有效
# server_bind()                               服务绑定
# verify_request(request, client_address)     验证请求

import socketserver


class MyTCPHander(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote".format(self.client_address[0]))
                print(self.data)
                # python2.7 是这样处理的，python3.0是通过try方式抓取的
                # if not self.data:
                #     print(self.client_address, "断开了")
                #     break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err", e)
                break


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    # 创建连接，主机，端口和自定义处理类
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHander)
    # 如果要支持多并发，则只需要改动为如下,这个是多线程并发
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHander)
    # 这个也是多并发，不过这个是多进程的方式，它和多线程并发效果是一样的，需要注意进程的方式只适合linux，window上无效
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHander)
    # 开始监听
    server.serve_forever()
