#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-14 15:40


import pickle

li = [11, 22, 33]
r = pickle.dumps(li)
print(r)

restult = pickle.loads(r)
print(restult)
