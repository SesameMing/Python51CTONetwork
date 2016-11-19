#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-27 22:32
# 学生：用户名、密码、性别、年龄、选课列表[]、上课记录{课程1：【di,a,】}
import time
import pickle

class student:

    def __init__(self, name, password, gender, age):
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.xuankelist = []
        self.shangkelist = {}

    def showxuanke(self):
        """ 显示选课列表 """
        print(self.xuankelist)

    def showshangke(self):
        """ 显示上课列表 """
        return self.shangkelist

    def addxuankelist(self, xuanke):
        """ 新增选课 """
        self.xuankelist.append(xuanke)
        return True

    def getxunkelist(self):
        """ 获取选课列表 """
        xuankelist = []
        for item in self.xuankelist:
            xuankelist.append(item.name)
        return xuankelist

    def addshangkelist(self, shangke):
        if len(self.shangkelist[shangke.name]) == 0:
            self.shangkelist[shangke.name] = []
        jl = [time.strftime("%Y-%m-%d", time.localtime()), shangke.name, shangke.teacher.name, shangke.shangkeneirong]
        self.shangkelist[shangke.name].append(jl)
        print(shangke.shangkeneirong)
        return True


    def getshangkelist(self):
        return self.shangkelist



