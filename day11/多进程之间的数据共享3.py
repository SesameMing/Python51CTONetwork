#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-18 16:41
# 在windows下不支持多进程，在linux下支持，
# windows下只能在 测试模式下使用
from multiprocessing import Process
from multiprocessing import Array


def foo(i, arg):
    arg[i] = i + 100
    for item in arg:
        print(item)
    print("================")


if __name__ == '__main__':
    li = Array('i', 10)
    for i in range(10):
        p = Process(target=foo, args=(i, li, ))
        p.start()
