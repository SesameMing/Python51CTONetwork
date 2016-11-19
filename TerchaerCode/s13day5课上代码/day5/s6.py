#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

import json

# dic = {'k1': 'v1'}
# print(dic,type(dic))
# # 将python基本数据类型转化成字符串形式
# result = json.dumps(dic)
# print(result,type(result))

# s1 = '{"k1": 123}'
# # 将python字符串形式转化成基本数据类型
# dic = json.loads(s1)
# print(dic,type(dic))








# import requests
# import json
#
# response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# response.encoding = 'utf-8'
#
# dic = json.loads(response.text)
# print(type(dic))

"""
import json
# py基本数据类型转换字符串
r = json.dumps([11,22,33])
# li = '["alex", "eric"]'
li = "['alex', 'eric']"
ret = json.loads(li)  # 反序列化时，一定要使用   "
print(ret,type(ret))
"""
import json
# li = [11,22,33]
# json.dump(li,open('db','w'))

# li = json.load(open('db','r'))
# print(type(li),li)




import pickle
# li = [11,22,33]
# r = pickle.dumps(li)
# print(r)
#
# result = pickle.loads(r)
# print(result)

# li = [11,22,33]
# pickle.dump(li, open('db', 'wb'))


# f = Foo()
# json.dumps(f)
# json._default_encoder
# result = pickle.load(open('db', 'rb'))
# print(result,type(result))

# json/pickle
# json更加适合跨语言，    基本数据类型
# pickle仅适用于python    pickle,python的所有类型的序列化，





