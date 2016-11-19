#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
class Foo:

    # 构造方法
    def __init__(self, name,age):
        self.name = name
        self.age = age

    # 析构方法
    def __del__(self):
        pass

    def __call__(self):
        print('call')

    def __str__(self):
        return "%s - %d" %(self.name, self.age)

    def __add__(self, other):
        temp = "%s - %d" %(self.name,other.age)
        return temp

    def __getitem__(self, item):
        # print(type(item),item)
        # item.start   item.stop  item.step
        print(type(item))
        return 123

    def __setitem__(self, key, value):
        # key.start   key.stop  key.step
        print(type(key),type(value))

    def __delitem__(self, key):
        # key.start   key.stop  key.step
        print(type(key))


obj = Foo('alex', 73)
# obj() # call
# 语法对应关系
# ret1 = obj['ad']
# ret2 = obj[1:4:2]
# obj[1:4] = [11,22,33,44,66]
# del obj[1:4]
# print(ret)
# obj['k1'] = 111
# del obj['k1']

# dic = {'k1': 123} # dic = dict(k1=123)
# dic['k1'] # dic()
# dic['k1'] = 123
# del dic['k1']


"""
obj = Foo()
obj() # 对象() 执行call
# Foo()()
"""
"""
obj1 = Foo('alex', 73)
obj2 = Foo('eric', 84)
# 获取对象中封装的数据
ret = obj1.__dict__
print(ret)
"""
# print(Foo.__dict__)

# print(obj1)
# print(obj2)

# ret = str(obj1)
# print(ret)

# ret = obj1 + obj2
# print(ret)
# __dict__

