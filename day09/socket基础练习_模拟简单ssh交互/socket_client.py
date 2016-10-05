#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-03 17:51
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

    # 解决粘包
    ready_tag = s.recv(1024)  # Ready|9998
    ready_tag = str(ready_tag, encoding='utf-8')

    if ready_tag.startswith('Ready'):
        msg_size = int(ready_tag.split('|')[-1])
    start_tag = 'Start'
    s.send(bytes(start_tag, encoding='utf8'))

    recv_size = 0
    recv_msg = b''
    while recv_size < msg_size:
        recv_data = s.recv(1024)
        recv_msg += recv_data
        recv_size += len(recv_data)
        print('MSG SIZE %s RECE SIZE %s' % (msg_size, recv_size))

    print(str(recv_msg, encoding='utf-8'))

s.close()
