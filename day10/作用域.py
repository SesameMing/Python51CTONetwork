#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-07 21:52

# li = [lambda :x for x in range(10)]
# print(li[0]())


li = []
for i in range(10):
    def f1():
        return i
    li.append(f1)
print(li[0]())


li = []
for i in range(10):
    def f1(x=i):
        return x
    li.append(f1)
print(li[0]())