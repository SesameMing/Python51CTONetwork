#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-28 20:16

# lambda表达式


def f1(a1):
    return a1 + 100


f2 = lambda a1, a2=9: a1 + 100

print(f1(2))
print(f2(2))
