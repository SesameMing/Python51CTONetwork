#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-12 17:26


def myrange():
    for i in range(10):
        yield i


def count(n):
    while n > 0:
        yield n   #生成值：n
        n -= 1


c = myrange()
for i in c:
    print(i)
