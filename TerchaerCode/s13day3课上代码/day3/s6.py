#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
#　abs绝对值
# n = abs(-1)
# print(n)

# all()
# any()

# 0，None,"", [], ()
# print(bool(()))
# 所有为真，才为真
# n = all([1,2,3,None])
# print(n)
# 只要有真，就为真
# n = any([[],0,"",None])
# print(n)
# ascii() # 自动执行对象的 __repr__
# class Foo:
#     def __repr__(self):
#         return "444"
#
# n = ascii(Foo())
# print(n)
# bin()
# oct()
# hex()
# print(bin(5))
# print(oct(9))
# print(hex(15))
"""
# utf-8 一个汉字：三个字节
# gbk 一个汉字：二个字节
# utf-8
s = "李杰"
# 一个字节8位，一个汉字三个字节
#  0101010 10101010 101010101  0101010 10101010 101010101
#     23     23      23           23     23      23  15
#     2f     2a      2c           2c     2e      2f  f
# 字符串转换字节类型
# bytes(只要转换的字符串， 按照什么编码）
n = bytes("李杰", encoding="utf-8")
print(n)
n = bytes("李杰", encoding="gbk")
print(n)
# 字节转化成字符串
new_str = str(bytes("李杰", encoding="utf-8"), encoding="utf-8")
"""
# 1、打开文件
# f = open('db', 'r') # 只读
# f = open('db', 'w') # 只写，先清空原文件
# f = open('db', 'x') # 文件存在，报错；不存在，创建并只写
# f = open('db', 'a') # 追加
# f = open('db','r', encoding="utf-8")
# data = f.read()
# print(data, type(data))
# f.close()

# f = open('db','r')
# data = f.read()
# print(data,type(data))

# f = open('db','rb')
# data = f.read()
# print(data,type(data))

# f = open("db", 'a')
# f.write("李杰")
# f.close()
#
# f = open("db", 'ab')
# f.write(bytes("李杰", encoding="utf-8"))
# f.close()
# f = open("db", 'r+', encoding="utf-8")
# # f.fileno()
# # 如果打开模式无 b，则read，按照字符读取
# data = f.read(1)
# # tell当前指针所在的位置（字节）
# print(f.tell())
# # 调整当前指着你的位置（字节）
# f.seek(f.tell())
# # 当前指针位置开始向覆盖
# f.write("888")
# f.close()

# 2、操作文件

# read() # 无参数，读全部；有参数，
#                                    b，按字节
#                                    无b，按字符
# tell() 获取当前指针位置(字节)
# seek(1) 指针跳转到指定位置(字节)
# write（） 写数据，b，字节；无b，字符
# close
# fileno
# flush 强刷
# readline 仅读取一行
# truncate 截断，指针为后的清空
# for循环文件对象 f = open(xxx)
# for line in f:
#     print(line)


# f = open("db", 'r+', encoding="utf-8")
# f.seek(3)
# f.truncate()
# f.close()
# f = open("db", 'r+', encoding="utf-8")
# for line in f:
#     print(line)



# 通过源码查看功能
# 3、关闭文件
# f.close()
# with open('xb') as f:
#     pass
with open('xb') as f:
    pass

with open('db1', 'r', encoding="utf-8") as f1, open("db2", 'w',encoding="utf-8") as f2:
    for line in f1:
        if line == "xx":
            f2.write()
            f2.write()
        # new_str = line.replace("alex", 'st')
        # f2.write(new_str)




# f = open("db", 'a',encoding="utf-8")
# f.write("123")
# f.flush()
# input("asdfasd")



