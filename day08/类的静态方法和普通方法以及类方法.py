#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-30 11:11


class Foo:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    @staticmethod  # 静态方法
    def f1():
        print(123)

    @classmethod  # 类方法 （静态方法的一种）
    def f2(cls):  # class
        # cls 类名 （） 创建对象
        print(cls)


# Foo.f1()
# Foo.f2()


