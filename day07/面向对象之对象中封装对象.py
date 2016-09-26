#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-26 19:34


class c1:

    def __init__(self, name, obj):
        self.name = name
        self.obj = obj

    def show(self):
        print(self.name)


class c2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)
        return True


c2_obj = c2('aa', 11)

c1_obj = c1('xx', c2_obj)
c1_obj.obj.show()
