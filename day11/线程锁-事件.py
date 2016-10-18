#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-17 18:51
import threading
import time


def func(i, e):
    print(i)
    e.wait()
    print(i+100)


even_obj = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(i, even_obj))
    t.start()

even_obj.clear()
inp = input(">>>:")
if inp == 'true':
    even_obj.set()
