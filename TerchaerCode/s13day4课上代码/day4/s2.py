#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

# def outer():
#     pass

# def outer(func):
#     print(123, func)
# def outer(func):
#     return "111"
#
# 定义函数，为调用，函数内部不执行
# 函数名 > 代指函数

def outer(func):
    def inner(*args, **kwargs):
        print('before')
        r = func(*args, **kwargs)
        print('after')
        return r
    return inner

# @ + 函数名
# 功能：
#     1. 自动执行outer函数并且将其下面的函数名f1当作参数传递
#     2. 将outer函数的返回值，重复赋值给 f1
@outer
def f1(arg):
    print(arg)
    return "砍你"

@outer
def f2(a1, a2):
    print("F2")

@outer
def f3():
    print("F3")