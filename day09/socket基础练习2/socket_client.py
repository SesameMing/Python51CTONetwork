#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-03 17:51
import socket
ip = '127.0.0.1'
port = 9999
s = socket.socket()
s.connect((ip, port))
while True:
    send_data = input(">>>:").strip()
    if send_data == 'exit':
        break
    if len(send_data) == 0:
        continue
    s.send(bytes(send_data, encoding='utf-8'))
    recv_data = s.recv(1024)
    print(recv_data)
s.close()