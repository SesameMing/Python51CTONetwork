#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-03 17:51
import socket
ip = '192.168.199.120'
port = 8000
s = socket.socket()
s.connect((ip, port))
recv_data = s.recv(1024).decode()
print(recv_data)
while True:
    send_data = input(">>>:").strip()
    if send_data == 'exit':
        break
    if len(send_data) == 0:
        continue
    s.send(bytes(send_data, encoding='utf-8'))
    recv_data = s.recv(1024).decode()
    print(recv_data)

s.close()
