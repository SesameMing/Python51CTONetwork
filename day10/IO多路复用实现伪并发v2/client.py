#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-12 10:36

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9999,))
data = sk.recv(1024)
print(data)
while True:
    inp = input(">>>:")
    sk.sendall(bytes(inp,encoding='utf8'))
    print(sk.recv(1024))
sk.close()