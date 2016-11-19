#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

class Foo:

    instance = None

    def __init__(self,name):
        self.name = name

    @classmethod
    def get_instance(cls):
        # cls类名
        if cls.instance:
            return cls.instance
        else:
            obj = cls("alex")
            cls.instance = obj
            return obj

obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
