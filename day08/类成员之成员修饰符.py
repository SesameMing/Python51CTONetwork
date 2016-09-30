#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-30 13:38


class Foo:

    __cc = "123"

    def __init__(self, name):
        self.__name = name

    def f1(self):
        print(self.__name)

    def f3(self):
        print(Foo.__cc)

    @staticmethod
    def f4():
        print(Foo.__cc)

    def __f5(self):
        print(self.__name)

    def f5(self):
        self.__f5()

obj = Foo('alex')


# 静态字段
obj.f3()
# or
Foo.f4()

obj.f5()

print(obj._Foo__name)  # 注意 不到万不得已 千万别用
