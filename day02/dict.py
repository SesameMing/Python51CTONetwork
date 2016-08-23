#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-23 21:49


dict = {1:'xxxxx',2:'2322222',3:{'name':'daming'}}#字典的创建
print(dict[1]) #字典的输出
dict[4] = 'yier' #字典的赋值
dict[1] = 'wwwww' #字典的修改
del dict[2] #字典的删除1
dict.pop(1) #字典的删除2
print(dict)
dict.get(1) #获取字典key的值
dict2 = {1:"love",4:{'name':'yier'}}
dict.update(dict2) #将dict2的值覆盖dict1
print(dict)
print(dict.items()) #将字典转为列表/元组
print(dict.values()) #打印字典中所有的value值
print(dict.keys()) #打印字典中所有的key值
#print(dict.has_keys()) #仅存在python2.x版本中 3.x版本中不存在改方法
dict.setdefault(2,'I') #取一个key的值，如果不存在就设置一个默认值
print(dict)
print(dict.fromkeys([1,2,3,4,5],'xxxxx')) #生成一个新的字典，和原本dict没任何关系。不建议使用
print(dict.popitem()) #随机删除字典中的某个key-value值
print(dict)

#循环字典的一种方法
for key in dict:
    print(key,'.', dict[key])
