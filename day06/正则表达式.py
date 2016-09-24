#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-23 21:56
import re
# 元字符
# . 通配符 除换行符以外的
# ^ 以什么开头
# $ 以什么结束
# * + ？ ｛｝ 都是代表重复
# * 匹配前一个0到多次重复
# + 匹配前一个1到多次重复
# ? 匹配前一个0或1次重复
# {} 匹配前一个如意次数或者范围
# []
# print(re.findall(r'I\b', 'I#am DamIng'))

s = "1+2+3*3/5"
r = re.search('[*/]', s, 1).group()
print(r)