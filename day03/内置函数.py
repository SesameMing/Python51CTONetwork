#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-28 20:24

# 内置函数

# 0, None, "", [], {}, () 是False

# abs()  # 绝对值 s = abs(-1)
# all()  # 所有为真，才为真
# any()  # 任何一个一个为真，就为真
# ascii()  # 自动执行对象的 __repr__方法
# bin()  # 十进制转二进制
# oct()  # 十进制转八进制
# hex()  # 十进制转十六进制
# bool()  # 布尔值
# bytes()  # 字符串转换字节类型
# bytearray()  #
# str()  # 字节转换成字符串


s = "中国"
n = bytes(s, encoding="utf-8")
y = bytearray(s, encoding="utf-8")
print(n)
print(y)

print(str(n,encoding="utf-8"))