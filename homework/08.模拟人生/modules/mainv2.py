#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-01 15:38
import sys
import time
from lib import Person


def timeprint(str):
    for i in str:
        time.sleep(0.3)
        print(i, end='')
        sys.stdout.flush()

print("(脑中自带键盘啪啦啪啦声响)")
print("故事背景：屌丝John，美女Liz，高富帅Peter。 John和Liz大学时是恋人，毕业工作后，Liz傍上了Peter，John伤心之余决定通过自己的努力追回Liz，多年后John通过努力变身高富帅，遇到被甩的Liz，Liz向John提出复合，John说……..")
John = Person.Person('John', '男', '18', '学生', '黄种人', '中国', '编程运维', 1000, 0, 0)
Liz = Person.Person('Liz', '女', '18', '学生', '黄种人', '中国', '逛街，购物', 1000, 0, 0)
Peter = Person.Person('Peter', '男', '18', '富二代', '黄种人', '中国', '泡妞', 2000000, 0, 0)
print(John)
print(Liz)
print(Peter)
print("John给Liz告白然后两人开始谈恋爱")
John.tanlianai(Liz)
print("John对象:", John.getduixiang())
print("毕业之后")
John.job = '网管'
Liz.job = '无业'
print("Liz傍上了Peter")
Liz.pitui(Peter)
print("Liz对象成了:", Liz.getduixiang())
print("John 就失恋了没有了对象", John.getduixiang())  # 而John 就失恋了
print("但是John奋发图强，去培训了Python")
print("过了5年")
Peter.addage(5)
Liz.addage(5)
John.addage(5)
John.nuli()
print(John)  # 成为了一个高富帅
print("Peter 分手 甩了Liz")
Peter.fenshou()
print("Liz向John提出复合，John说:我已经有爱我支持我的人了。")
print("John 从此迎娶白富美，走向人生巅峰。")



