#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-28 17:45



# def f1():
#     print(1)
# def f1():
#     print(2)
# f1()


# def f1(a1):
#     print(id(a1))
#     a1.append(999)
# li = [11,22,33,44]
# print(id(li))
# f1(li)
# print(li)


#   全局变量，所用作用域都是可读的
#   特殊：列表字典，可以修改，不可重新赋值
#   对全局变量进行重新赋值，需要global
#   默认规则，定义全局变量全部大写

NAME = "daming"

def f1():
    age = 10
    name = "123"
    print(NAME, age)

def f2():
    age = 19
    print(NAME, age)

def f3():
    global NAME  # 定义变量 name 为全局变量
    NAME = "szy"
    age = 18
    print(NAME, age)
f1()
f2()
f3()
print(NAME)