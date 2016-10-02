#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-30 23:19

class Foo:
    instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls, name):
        if cls.instance :
            return cls.instance
        else:
            obj = cls(name)
            cls.instance = obj
            return obj

obj1 = Foo.get_instance('alex')
print(obj1)

obj2 = Foo.get_instance('www')
print(obj2)