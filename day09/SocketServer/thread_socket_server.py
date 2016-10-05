#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-05 15:29
import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        self.request.sendall(bytes('欢迎致电 10086,请输入1xxx,0转人工服务.', encoding='utf-8'))
        while True:
            data = self.request.recv(1024)
            print("[%s] says: %s" % (self.client_address, data.decode()))
            self.request.sendall(data.upper())


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), MyServer)
    server.serve_forever()
