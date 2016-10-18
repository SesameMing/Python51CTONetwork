#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-18 16:41
# 在windows下不支持多进程，在linux下支持，
# windows下只能在 测试模式下使用
from multiprocessing import Process

def foo(i):
    print('say hi', i)


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.start()
