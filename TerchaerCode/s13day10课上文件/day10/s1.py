#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# Python中无块级作用域

# if 1 == 1:
#     name = 'alex'
# for i in range(10):
#     name = i
# print(name)

# Python中以函数为作用域

# def func():
#     name = 'alex'
#
# print(name)
# def func():
#     name = 'alex'
# func()
# print(name)

# name = 'alex'
#
# def f1():
#     name = 'eirc'
#     print(name)
# f1()
# Python作用域链，由内向外找，直到找不到报错
# name = 'alex'
# def f1():
#     # name = 'a'
#     def f2():
#         # name = 'b'
#         print(name)
#     f2()
# f1()


# python的作用域在执行之前已经确定
"""
name = "alex"
def f1():
    print(name)

def f2():
    name = 'eric'
    f1()
# f2()



name = 'alex'
def f1():
    print(name)

def f2():
    name = 'eric'
    return  f1

ret = f2()
ret()

"""
# li = [x for x in range(10)]
# li = [x+100 for x in range(10) if x > 6]
# print(li)
# def f1():
#     return x
# li = [lambda :x for x in range(10)]
# li列表
# li列表中的元素：【函数，函数，函数...】
# 函数在没有执行前，内部代码不执行
# ？li[0]，函数
# ？函数()
# 返回值是？？？？
# r = li[0]()
# print(r)

# li = []
#
# for i in range(10):
#     def f1(x=i):
#         return x
#     # li.append(i+1)
# # li是列表，内部元素是相同功能的函数
# # i
# print(li[0]())
# print(li[1]())
# print(li[2]())




