#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-30 21:58


class C1:
    def f1(self):
        print('c1,f1')


class C2(C1):
    def f1(self):
        # # 执行父类的f1方法 1
        # super(C2, self).f1()
        # print('c2.f1')

        # 执行父类的f1方法 2 不建议
        C1.f1(self)


obj = C2()
obj.f1()