#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 10:28

import contextlib
import socket


@contextlib.contextmanager
def context_socket(host, port):
    sk = socket.socket()
    sk.bind((host, port))
    sk.listen(5)
    try:
        yield sk
    finally:
        sk.close()

with context_socket('127.0.0.1', 8888) as sock:
    print(sock)

