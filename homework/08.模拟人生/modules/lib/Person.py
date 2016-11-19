#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-01 15:39


class Person:

    def __init__(self, name, garden, age, job, renzhong, guoji, techang, money, fang, che):
        self.name = name
        self.garden = garden
        self.age = age
        self.job = job
        self.renzhong = renzhong
        self.guoji = guoji
        self.techang = techang
        self.money = money
        self.fang = fang
        self.che = che
        self.duixiang = None

    # 谈恋爱
    def tanlianai(self, obj):
        self.duixiang = obj
        obj.duixiang = self

    # 获取对象
    def getduixiang(self):
        if self.duixiang:
            return self.duixiang.name
        else:
            return None

    # - -劈腿，额这么写好吗
    def pitui(self, newobj):
        self.duixiang.duixiang = None
        self.duixiang = newobj
        newobj.duixiang = self
        print("%s 劈腿和%s在一起了" % (self.name, newobj.name))

    # 分手
    def fenshou(self):
        print("%s 和 %s 分手了" % (self.name, self.duixiang.name))
        self.duixiang.duixiang = None
        self.duixiang = None


    # 过了好几年
    def addage(self, age):
        self.age = int(self.age) + int(age)

    # 人物介绍
    def rwjs(self):
        print("%s,年龄：%s, 是一个%s，资产：%s" % (self.name, self.age, self.job, self.money))

    # 不误正业
    def buwuzhengye(self):
        self.money = int(self.money) - 1000


    # 努力奋斗 加金币
    def nuli(self):
        self.money += int(self.money) + 1000000
        self.fang += int(self.fang) + 1
        self.che += int(self.che) + 1

    def __str__(self):
        if self.garden == '男':
            if int(self.money) <= 1000000:
                return "%s 是个屌丝 %s" % (self.name, self.job)
            else:
                return "%s 是个高富帅 %s" % (self.name, self.job)
        else:
            return "%s 是个美女 %s" % (self.name, self.job)


if __name__ == '__main__':
    John = Person('John', '男', '18', '网管', '黄种人', '中国', '编程运维', 1000, 0, 0)
    print(John.__dict__)