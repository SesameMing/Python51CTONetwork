#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-03 17:48
import socket
import subprocess
ip = '127.0.0.1'
port = 9999
s = socket.socket()
s.bind((ip, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    while True:
        try:
            recv_data = conn.recv(1024)
            if len(recv_data) == 0:
                break
            print("收到来自", addr, "的消息：", str(recv_data, encoding='utf-8'))
            p = subprocess.Popen(str(recv_data, encoding='utf-8'), shell=True, stdout=subprocess.PIPE)
            res = p.stdout.read()
            if len(res) == 0:
                send_data = 'cmd error'
            else:
                send_data = str(res, encoding='gbk')
            conn.send(bytes(send_data, encoding='utf-8'))
        except Exception:
            break
    conn.close()

