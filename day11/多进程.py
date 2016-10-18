#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-18 16:41

from multiprocessing import Process


def foo(i):
    print('say hi', i)


for i in range(10):
    p = Process(target=foo, args=(1,))
    p.start()
