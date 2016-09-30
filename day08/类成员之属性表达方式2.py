#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-30 13:17

class Pager():
    def __init__(self, all_count):
        self.all_count = all_count

    def f1(self):
        return 123

    def f2(self):
        pass

    def f3(self):
        pass

    foo = property(fget=f1, fset=f2, fdel=f3)

p = Pager(101)

result = p.foo
print(result)

p.foo = 'alex'

del p.foo
