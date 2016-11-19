#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

# class Foo:
#     # 字段（静态字段）
#     CC = 123
#
#     def __init__(self):
#         # 字段（普通的字段）
#         self.name = 'alex'
#
#     def show(self):
#         print(self.name)


class Province:
    country = "中国"

    def __init__(self,name):
        self.name = name
    # 普通方法，由对象去调用执行（方法属于类）

    def show(self):
        # print(self.name)
        print(123)

    @staticmethod
    def f1(cla,a1,a2):
        # 静态方法，由类调用执行。（当方法内部不需要对象中封装的值时，可以将方法写成静态方法）
        print(a1,a2)

    @classmethod
    def f2(cls):# class
        cls # 类名，（）创建对象
        # cls()
        print(cls)

    def f3(self):
        return self.name[1]



# obj = Province("河南")
# obj.show()
# Province.f1(Province,1,2)
# Province.f2()

# obj = Province('alex')
# ret = obj.f3()
# print(ret)




class Pager:

    def __init__(self, all_count):
        self.all_count = all_count

    def f1(self):
        return 123

    def f2(self,value):
        pass

    def f3(self):
        pass

    foo = property(fget=f1,fset=f2, fdel=f3)

p = Pager(101)

result = p.foo
print(result)
p.foo = "alex"
del p.foo









