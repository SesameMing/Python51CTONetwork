#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

class Foo:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

# import pickle
#
# obj = Foo('alex')
# pickle.dump(obj, open('db','wb'))
