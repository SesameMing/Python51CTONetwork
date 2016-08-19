#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-19 23:25

namelist = ["wm","szy","son","laocai","1","2","3","4","5","6","7","8","9"]
print(namelist)
namelist.insert(4,"xxxx")
namelist.insert(5,"yyyy")
print(namelist)
namelist.remove(namelist[6])
print(namelist)
del namelist[4:6]
print(namelist)
namelist[0]="wm组长"
print(namelist[::2])

print(namelist)

if 'szy' in namelist: #判断是否在列表里
    print("存在")

print(namelist.count('4')) #计算列表中某个元素的个数
print(namelist.index("4")) #返回查找的第一个元素的索引

for i in range(namelist.count("4")):
    namelist[namelist.index("4")] = 444444444
print(namelist)