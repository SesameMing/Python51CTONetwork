#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

"""
def f1():
    pass
# f1()

f2 = 123
# f2()

print(callable(f1))
print(callable(f2))
"""
# chr()
# ord()
# r = chr(65)
# print(r)
#
# n = ord("a")
# print(n)



# 1=<i<5
# i = random.randrange(65, 91)
# c = chr(i)
# print(c)

# import random
# li = []
#
# for i in range(6):
#     if i ==2 or i == 4:
#         num = random.randrange(0, 10)
#         li.append(str(num))
#     else:
#         temp = random.randrange(65, 91)
#         c = chr(temp)
#         li.append(c)
#
# result = "".join(li)
# print(result)


"""
import random
li = []

for i in range(6):
    r = random.randrange(0, 5)
    if r ==2 or r == 4:
        num = random.randrange(0, 10)
        li.append(str(num))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)

result = "".join(li)
print(result)
"""
#
# compile()
# eval()
# exec()

s = "print(123)"

# 编译，single，eval，exec
# 将字符串编译成python代码
# r = compile(s, "<string>", "exec")

# 执行python代码
# exec(r)

# s = "8*8"
# ret = eval(s)
# print(ret)
# 将字符串，编译成python代码
# compile()

# # 执行python代码，接收：代码或者字符串
# exec("7+9+8")
# # 执行表达式，并且获取结果
# ret = eval("7+9+8")
# print(ret)

# 快速查看，对象提供了那些功能
# print(dir(list))
# help(list)

# 共：97， 每页显示10条，需要多少页
# r = divmod(100, 10)
# print(r[0])
# print(r[1])

# n1, n2 = divmod(100, 10)

#
# s = "alex" # 对象，"alex" => str

# s = [11,11,11]
# # 用于判断，对象是否是某个类的实例
# r = isinstance(s, list)
# print(r)

# filter,map


# def f1(args):
#     result = []
#     for item in args:
#         if item > 22:
#             result.append(item)
#     return result
#
# li = [11, 22, 33, 44, 55]
# ret = f1(li)
# print(ret)

# filter(函数，可迭代的对象)
# def f2(a):
#     if a>22:
#         return True
# li = [11, 22, 33, 44, 55]
# filter内部，循环第二个参数
# result = []
# for item in 第二个参数:
#     r = 第一个参数(item)
#     if r :
#         result(item)
# return result
# filter ，循环循环第二个参数，让每个循环元素执行 函数，如果函数返回值True，表示元素合法
# ret = filter(f2, li)
# print(list(ret))

# filter,内部循环，参数比较

# 自动return
# f1 = lambda a: a > 30
#
# ret = f1(10)
# print(ret)

# li = [11, 22, 33, 44, 55]
# result = filter(lambda a: a > 33, li)
# print(list(result))



# map

li = [11, 22, 33, 44, 55]

# map(函数，可迭代的对象(可以for循环的东西))
# def f2(a):
#     return a + 100

# result = map(f2, li)
# result = map(lambda a: a + 200, li)
# print(list(result))

# filter  # 函数返回True，将元素添加到结果中
# map     # 将函数返回值添加到结果中

# def f1(args):
#     result = []
#     for i in args:
#         result.append(100+i)
#
#     return result
# r = f1(li)
# print(list(r))



# set

# NAME = "ALEX"
#
# def show():
#     a = 123
#     c = 123
#     print(locals())
#     print(globals())
#
# show()


# s = "hhhasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfhhhasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"
# dic = {
#     6366645726074670325:1
# }
# print(hash(s))

# s = "李杰"
# print(len(s))
#
# s = "李杰"
# b = bytes(s, encoding='utf-8')
# print(len(b))

# 2.7 for “李杰”
# 3.5 for “李杰”


# r = sum([11,22,33,1])
# print(r)

# str,

# r = repr("alex")
# print(r)

# li = [11,22,1,1]
#
# # li.reverse()
#
# reversed(li)

# r = round(1.4)
# print(r)
# s = "sssssssss"
# print(s[0:2:2])

# li = [11,2,1,1]
# li.sort()
#
# sorted(li)
#
# l1 = ["alex", 11, 22, 33]
# l2 = ["is", 11, 22, 33]
# l3 = ["sb", 11, 22, 33]
#
# r = zip(l1, l2, l3)
# temp = list(r)[0]
# ret = ' '.join(temp)
# print(ret)

class Foo:
    pass


# print(Foo())
print(Foo)