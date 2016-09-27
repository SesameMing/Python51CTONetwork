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

    def __init__(self, name, age, gender, money):
        self.name = name
        self.age = age
        self.gender = gender
        self.money = money

    def getmoney(self, value):
        print("老师获得money")
        self.money += value



