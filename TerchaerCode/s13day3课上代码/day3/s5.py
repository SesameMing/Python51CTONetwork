#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

# 三元运算，三目运算，if else简写
"""
if 1 == 1:
    name = "alex"
else:
    name = "SB"
# 如果 1==1 成立，
# name = "alex"
# 否则
# name = "SB"
name = "alex" if 1 == 1 else "SB"
"""

def f1(a1):
    return a1 + 100

f2 = lambda a1, a2=9: a1 + a2 + 100

ret = f1(10)
print(ret)

r2 = f2(9)
print(r2)







