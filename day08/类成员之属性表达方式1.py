#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-30 13:17

class Pager():
    def __init__(self, all_count):
        self.all_count = all_count

    @property
    def all_pager(self):
        a1, a2 = divmod(self.all_count, 10)
        if a2 == 0:
            return a1
        else:
            return a1 + 1

    @all_pager.setter
    def all_pager(self, value):
        print(value)

    @all_pager.deleter
    def all_pager(self):
        print("all_pager")


p = Pager(101)
# p.all_count  # 字段
# result = p.all_pager()  # 方法
# print(result)
# print(p.all_count)
# p.all_count = 102
# del p.all_count


# ret = p.all_pager
# print(ret)
# p.all_pager = 111
# del p.all_pager

