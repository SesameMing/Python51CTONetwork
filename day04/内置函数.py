#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-03 17:33


# s = "print(123)"
# # 编译 编译模式： single,eval,exec
# r = compile(s, '<string>', "exec")
# # 执行
# exec(r)
# s = "8*8"
# ret = eval(s)
# print(ret)

# compile() 编译
# exec 执行python代码, 接收：代码或者字符串
# eval 执行 执行表达式，是有返回值

#
# r = divmod(97, 10)
# print(r)
# #输出(商，余数)
#
# s = [11,22,11,22]
# r = isinstance(s, list)
# print(r)


# filter, map

# filter(函数, 可迭代的对象)
def f2(a):
    if a > 22:
        return True

li = [11, 22, 33, 44, 55, 66]
ret = filter(f2, li)
print(list(ret))

