#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-04 10:11


def outer(func):
    def inner():
        print('log')
        rs = func()
        print('before')
    return inner


@outer
def f1():
    print("F1")


@outer
def f2():
    print("F2")


f1()