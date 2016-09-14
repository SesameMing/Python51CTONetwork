#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-14 12:24

import json

dic = {'k1': 'v1'}
print(dic, type(dic))
# 将python的基本数据类型转换成字符串形式
result = json.dumps(dic)
print(result, type(result))

#  将python字符串形式转换成基本数据类型
s1 = '{"k1": 123}'
dic1 = json.loads(s1)
print(dic1, type(dic1))

li = [11, 22, 33]
json.dump(li, open('db', 'w'))

li = json.load(open('db', 'r'))
print(li, type(li))
