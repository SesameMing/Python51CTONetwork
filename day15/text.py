#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-12-14 17:16
import os
print(os.path.join(os.getcwd(), 'xxxx.text'))
print(__file__)
print(os.path.join(os.path.dirname(__file__), 'xxxx.text'))
print(os.path.abspath(__file__))