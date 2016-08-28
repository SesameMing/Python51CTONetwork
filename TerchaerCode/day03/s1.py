#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# 1、set，无序，不重复序列
# li = [11,222]
# print(li)
# a. 创建
# li = []
# list((11,22,33,4))
# list __init__,内部执行for循环(11,22,33,4)  [11,22,33,4]
# 原理，list
# dic = {"k1":123}
# se = {"123", "456"}
# s = set() # 创建空集合
# li = [11,22,11,22]
# s1 = set(li)
# print(s1)
# b. 功能
# set()\


# 创建集合
# s1 = {11,22}
# s2 = set()
# s3 = set([11,22,33,4])

## 操作集合
# s = set()
# print(s)
# s.add(123)
# s.add(123)
# s.add(123)
# print(s)
# s.clear()
# print(s)


# s1 = {11,22,33}
# s2 = {22,33,44}
# s3 = s1.difference(s2)
# A中存在，B中不存在
# s3 = s2.difference(s1)
# s3 = s1.symmetric_difference(s2)
# print(s1)
# print(s2)
# print(s3)
# s1.difference_update(s2)
# s1.symmetric_difference_update(s2)
# print(s1)

# s1 = {11,22,33}
# s1.discard(1111)
# s1.remove(11111)
# ret = s1.pop()
# print(s1)
# print(ret)

# s1 = {11,22,33}
# s2 = {22,33,44}
# s3 = s1.union(s2)
# print(s3)
# s3 = s1.intersection(s2)
# s1.intersection_update(s2)
# print(s3)
"""
s1 = {11,22,33}
s1.add(11)
s1.add(12)
s1.add(13)
# li = [11,22,3,11,2]
# li = (11,22,3,11,2)
li = "alexalex"
s1.update(li)
print(s1)
"""

# li = [11,22,33] # list __init__
# li()            # list __call__
# li[0]           # list __getitem__
# li[0] = 123     # list __setitem__
# def li[1]       # list __delitem__
old_dict = {
    "#1": 8,
    "#2": 4,
    "#4": 2,
}

new_dict = {
    "#1": 4,
    "#2": 4,
    "#3": 2,
}
# old_kyes = old_dict.keys()
# old_set = set(old_kyes)
new_set = set(new_dict.keys())
old_set = set(old_dict.keys())

remove_set = old_set.difference(new_set)
add_set = new_set.difference(old_set)
update_set = old_set.intersection(new_set)


import re
re.match()