#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-05 23:48
import socket

myname = socket.gethostname()
myaddr = socket.gethostbyname(myname)
print(myname)
print(myaddr)

def main():
    pass


def run():
    print("服务端开启")
    print("正在初始化软件")
    server_name = socket.gethostname()
    ip = socket.gethostbyname(server_name)


if __name__ == '__main__':
    run()