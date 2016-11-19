#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)
while True:
    conn, address = sk.accept()
    conn.sendall(bytes('hello', encoding='utf-8'))
    while True:
        recv_bytes = conn.recv(1024)
        if str(recv_bytes,encoding='utf-8') == 'q':
            break
        conn.sendall(recv_bytes)