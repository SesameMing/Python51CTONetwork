#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

class Foo:

    def __init__(self, name):
        self.__name = name

    def f1(self):
        print(self.__name)


# obj = Foo("alex")
# print(obj.__name)
# print(obj._Foo__name)