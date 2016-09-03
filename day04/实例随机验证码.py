#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-03 16:27

# import random
# r = random.randrange(65, 91)
# print(r)
# print(chr(r))
# li = []
# for i in range(6):
#     temp = random.randrange(65, 91)
#     c = chr(temp)
#     li.append(c)
# result = "".join(li)
# print(result)


import random
r = random.randrange(65, 91)
li = []
for i in range(6):
    r = random.randrange(0, 5)
    if r == 2 or r == 4:
        temp = random.randrange(0, 10)
        li.append(str(temp))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)
result = "".join(li)
print(result)
