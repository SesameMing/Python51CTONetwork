#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-26 20:04


class F1:  # 父类，基类
    def show(self):
        print('show')


class F2(F1):  # 子类，派生类
    def bar(self):
        print('show')


class F3(F2):
    pass


sbj = F2()
sbj.show()