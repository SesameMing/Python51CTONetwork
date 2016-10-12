#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-11 18:26

import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)

inputs = [sk, ]
while True:
    rlist, w, e = select.select(inputs, [], [], 1)
    print(len(inputs), len(rlist))
    for r in rlist:
        if r == sk:
            conn, address = r.accept()
            inputs.append(conn)
            conn.sendall(bytes('hello', encoding='utf-8'))
        else:
            print("============")
            try:
                ret = r.recv(1024)
                r.sendall(ret)
                if not ret:
                    raise Exception('断开连接')

            except Exception as e:
                inputs.remove(r)


