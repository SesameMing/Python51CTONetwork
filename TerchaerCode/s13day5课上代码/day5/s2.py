#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# %s %d

# s = "阿朵发送到 %s adfa %d" %('laex', 123)
# print(s)

# s = "asdf%(name)-10saaa %(age)-10d   %(p).2f" %{'name':'alex','age': -123, "p": 1.236567}
# print(s)

# s  = "asdifuyaksdf %c ---- %o  ===== %x ===== %g" %(65, 15, 15, 100)
# print(s)
# s1 = "alex %"
# print(s1)
# 当格式化时，字符串中出现占位符 %s.. 需要用 %% 输出 %
# s2 = "alex %s %%" %('SB')
# print(s2)


# s1 = "asdfasdf{0}a123{0}123{1}".format(123, "alex")
# print(s1)
# s1 = "----{name:s}____{age:d}===={name:s}".format(name='alex', age=123)
# print(s1)

# s2 = "----{:*^20s}====={:+d}===== {:x}".format('alex', 123, 15)
# print(s2)

# s3 = "asdfasdfasd {:.2%}".format(0.234567)
# print(s3)


# li = [11,22,33,44]
# li = [11,22,33,44]
# result = filter(lambda x:x>22, li)
# print(result) # 具有生成指定条件数据的能力的一个对象
#


# 生成器，使用函数创造

# 普通函数
# def func():
#     return 123
#
# ret = func()
"""
def func():
    print(1111)
    yield 0
    print(222)
    yield 2
    print(333)
    yield 9

ret = func()
r1 = ret.__next__() # 进入函数找到yield，获取yield后面的数据
print(r1)
r2 = ret.__next__() # 进入函数找到yield，获取yield后面的数据
print(r2)
r3 = ret.__next__() # 进入函数找到yield，获取yield后面的数据
print(r3)
r4 = ret.__next__() # 进入函数找到yield，获取yield后面的数据
print(r4)
"""
# def myrange(arg):
#     start = 0
#     while True:
#         if start > arg:
#             return
#         yield start
#         start += 1
#
# ret = myrange(3)
# for item in ret:
#     print(item)

# 无返回值，None
"""
def d():
    return '123'

def c():
    r = d()
    return r

def b():
    r = c()
    return r

def a():
    r = b()
    print(r)
a()
"""

def func(n):
    n +=1
    if n >= 4:
        return 'end'
    return func(n)

r = func(1)
print(r)





