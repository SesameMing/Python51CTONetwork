#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

class A(object):
    def f1(self):
        print('A')

class B(A):
    def f2(self):
        print('B')
class C(A):
    def f1(self):
        print('C')

class D(B):
    def f2(self):
        print('D')

class E(C):
    def f1(self):
        print('E')

class F(D,E):
    def f2(self):
        print('f')

obj = F()
obj.f1()