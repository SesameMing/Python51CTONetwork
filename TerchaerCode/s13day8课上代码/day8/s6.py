#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# li = list([11,22,33,44])
#
# for item in li:
#     print(item)
# class Bar:
#     pass
#
# class Foo(Bar):
#
#     pass
#
# obj = Foo()
# obj,Bar（obj类型和obj类型的父类）的实例
# ret = isinstance(obj, Bar)
# print(ret)
# ret = issubclass(Bar,Foo)
# print(ret)








class C1:

    def f1(self):
        print('c1.f1')
        return 123

obj = C1()
C1.f1(obj)
obj.f1()

class C2(C1):

    def f1(self):
        # 主动执行父类的f1方法
        ret = super(C2,self).f1()
        super(C2, self).f1()
        print('c2.f1')
        return ret

        # C1.f1(self)

obj = C2()
obj.f1()













