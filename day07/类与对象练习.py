#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-26 19:05


class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def kanchai(self):
        print("%s, %s岁, 上山去砍柴" % (self.name, self.age))

    def kaiche(self):
        print("%s, %s岁, 开车去东北" % (self.name, self.age))

    def dabaojian(self):
        print("%s, %s岁, 最爱大保健" % (self.name, self.age))


laozhang = Foo('老张', '90')
laozhang.kanchai()
laozhang.kaiche()
laozhang.dabaojian()

