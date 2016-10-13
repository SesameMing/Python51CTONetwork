#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-05 15:29
import socketserver
import subprocess


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        self.request.sendall(bytes('欢迎致电 10086,请输入1xxx,0转人工服务.', encoding='utf-8'))
        print("%s 链接了服务端" % self.client_address[0])
        while True:
            data = self.request.recv(1024)
            print("[%s] says: %s" % (self.client_address, data.decode()))
            # self.request.sendall(data.upper())
            cmd = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            cmd_res = cmd.stdout.read()
            if not cmd_res:
                cmd_res = cmd.stderr.read()
            if len(cmd_res) == 0:  # cmd has mot output
                cmd_res = "没有这个命令"
                cmd_res = bytes(cmd_res, encoding='utf8')
            self.request.sendall(cmd_res)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 8009), MyServer)
    server.serve_forever()
