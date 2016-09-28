#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-27 15:11
"""
这是一个老师类
"""
import pickle


class teacher:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.money = 0

    def getmoney(self, value):
        print("老师获得money")
        self.money += value

    def userinfo(self):
        info = {'name': self.name, 'age': self.age, 'gender': self.gender, 'money': self.money}
        return info

    def getname(self):
        return self.name




