#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
"""
我是注释
"""

# print(__doc__)
# __cached__
# from bin import admin
# print(__file__)
# print(__package__)
# print(admin.__package__)
# 只有执行当前文件时候，当前文件的特殊变量 __name__ == "__main__"
# __name__ == __main__

# def run():
#     print('run')
#
# if __name__ == "__main__":
#     run()
# import os
# print(os.pathsep)
import hashlib

obj = hashlib.md5(bytes('kajasdfasdfasdfasdfsadfasdfsadfshdfnasdkf', encoding='utf-8'))
obj.update(bytes('123', encoding='utf-8'))
result = obj.hexdigest()
print(result)