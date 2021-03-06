#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-26 18:01

# set,集合,无序，不重复序列

'''
# 创建
li = []  # 列表
dic = {}  # 字典
se = {"123", "456"}  # 集合 创建集合方式1
s = set()  # 创建一个空集合 创建集合方式2
li = [11, 22, 11, 22]
s1 = set(li)  # 将列表转化成集合 创建集合方式3
print(s1)
'''()
# 功能


## 操作集合
s = set()

s.add(123)  # 添加元素
s.clear()  # 清除元素

s1 = {11,22,33}
s2 = {22,33,44}
s3 = s1.difference(s2)  # s1中存在，s2中不存在 赋值给新的变量s3
s3 = s1.symmetric_difference(s2)  # s1存在s2中不存的 和 s2中存在s1中不存的 赋值给新的变量s3
s1.difference_update(s2)  # s1中存在，s2中不存在 更新到s1
s1.symmetric_difference_update(s2)  # s1存在s2中不存的和s2中存在s1中不存的更新到s1
s1.discard(11)  # 移除指定元素，不存在不报错
s1.remove(11)  # 移除指定元素，不存会报错
s1.pop()  # 移除某个元素，并返回这个元素
s1.intersection(s2)  # 取两个的交集 赋值给新的变量s3
s1.intersection_update(s2 )  # 取两个的交集,更新给s1
s1.isdisjoint(s2)  # 判断两个集合有没有交集
s1.issubset(s2)  # 是否是子序列
s1.issuperset(s2)  # 是否是父序列
s3 =  s1.union(s2)  # 并集
s1.update()  # 更新，接受一个可以迭代的对象，可以是list，元组，字符串