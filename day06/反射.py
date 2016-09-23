#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-23 14:12

inp = "accp/index"
m, f = inp.split('/')
obj = __import__(m)
if hasattr(obj, f):
    func = getattr(obj, f)
    func()
else:
    print('404')


# 如果模块在lib文件夹中
obj = __import__("lib." + m, fromlist=True)