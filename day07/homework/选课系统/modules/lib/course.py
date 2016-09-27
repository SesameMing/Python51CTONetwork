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
    def __init__(self, name, time, money, teacher ,shangkeneirong):
        self.name = name
        self.time = time
        self.money = money
        self.teacher = teacher
        self.shangkeneirong = shangkeneirong

    def shangke(self):
        print("今天学习了", self.shangkeneirong)
