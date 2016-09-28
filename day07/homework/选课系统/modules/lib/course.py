#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-27 22:16
# 创建课程：课程名称、上课时间、课时费、关联老师
"""
这是一个课程类
"""


class course:

    def __init__(self, name, money, teacher, shangkeneirong):
        self.name = name
        self.time = 0
        self.money = money
        self.teacher = teacher
        self.shangkeneirong = shangkeneirong

    def shangke(self):
        print("今天学习了", self.shangkeneirong)

    def courseinfo(self):
        cinfo = {'name': self.name, 'money': self.money, 'teacher': self.getteacher(), 'shangkeneirong': self.shangkeneirong}
        return cinfo

    def getteacher(self):
        return self.teacher.getname()