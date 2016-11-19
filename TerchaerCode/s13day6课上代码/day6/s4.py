#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import re
# origin = "hasaabc dfuojqw halaabc m098u2934l"
# # r = re.match("h\w+", origin)
# # r = re.match("h(\w+)", origin)
# r = re.findall("h(\w+)a(ab)c", origin)
# print(r)
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果
# print(r.groupdict()) # 获取模型中匹配到的分组结果
 # 无分组
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("a(le)x", origin, 1)
print(r)

# 有分组
#
# origin = "hello alex bcd alex lge alex acd 19"
# r1 = re.split("(alex)", origin, 1)
# print(r1)
# r2 = re.split("(al(ex))", origin, 1)
# print(r2)