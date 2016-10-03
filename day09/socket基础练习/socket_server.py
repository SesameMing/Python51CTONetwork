#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-03 17:48
import socket
ip = '127.0.0.1'
port = 9999

s = socket.socket()
s.bind((ip, port))
s.listen(5)
conn, addr = s.accept()
recv_data = conn.recv(1024)
conn.send(recv_data)
conn.close()


