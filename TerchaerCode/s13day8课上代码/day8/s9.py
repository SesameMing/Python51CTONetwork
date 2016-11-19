#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# while True:
#     num1 = input('num1:')
#     num2 = input('num2:')
#     try:
#         li = []
#         li[100]
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#
#     except ValueError as ex:
#         print(ex) # str
#     except IndexError as ex:
#         print(ex) # str
#     except Exception as ex:
#         print(ex)


# try:
#     raise ValueError('主动错误一下') # self.message = '主动错误一下'
#     print(1234)
# except ValueError as ex:
#     print(ex) # str
# except Exception as ex:
#     print(ex) # __str__, return self.message
# else:
#     pass
# finally:
#     pass


# assert 1==1

p = object()
p.status = True
p.start() # 应该先执行一个 assert p.status == False

import multiprocessing

from multiprocessing import pool

b = pool.Pool()

b.join()




