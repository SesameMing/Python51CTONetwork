#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-27 22:32
# 学生：用户名、密码、性别、年龄、选课列表[]、上课记录{课程1：【di,a,】}
class student:
    def __init__(self, name, password, gender, age):
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.xuankelist = []
        self.shangkelist = []

    def showxuanke(self):
        """ 显示选课列表 """
        print(self.xuankelist)

    def showshangke(self):
        """ 显示上课列表 """
        print(self.shangkelist)

    def setxuankelist(self, xuanke):
        self.xuankelist = xuanke

    def addshangkelist(self, shangke):
        self.shangkelist.append(shangke)


