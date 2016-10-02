#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-30 14:20


class Foo:
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__")

    # 析构方法
    def __del__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("__call__")

    def __str__(self):
        return '__str__'

    def __add__(self, other):
        tmp = "%s-%d , %s-%d" % (self.name, self.age, other.name, other.age)
        return tmp

    def __getitem__(self, item):
        print(1111)
        pass

    def __setitem__(self, key, value):
        print('__setitem__')

    def __delitem__(self, key):
        print('del item')


obj1 = Foo('alex', 73)  # 类后面加（） 执行 __init__() 方法
obj2 = Foo('eric', 84)
obj1()  # 对象() 执行 __call__() 方法
print(obj1)

ret = obj1 + obj2  # 两个对象相加 执行 obj1的__add__（）方法
print(ret)

# __dict__
# 获取对象中封装的数据
ret = obj1.__dict__
print(ret)
print(Foo.__dict__)

obj1['ad']  # 对象['XXX'] 自动用的 __getitem__()方法
obj1['k1'] = 111 # 对象['XXX']=111 自动用的 __setitem__()方法
del obj1['k1'] # del 对象['XXX'] 自动用的 __delitem__()方法'
obj[1:2]  # 执行__getitem__()方法