#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-17 21:39
import threading


def func(i,conn):
    print(i)
    conn.acquire()
    conn.wait()
    print(i+100)
    conn.release()



conn = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(i, conn))
    t.start()

while True:
    inpp = input(">>>>")
    if inpp == 'q':
        break
    conn.acquire()
    conn.notify(int(inpp))
    conn.release()