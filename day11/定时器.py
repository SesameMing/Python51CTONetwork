#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-17 21:44
import threading


def do():
    print("xxxxxxxxx")

t = threading.Timer(1, do)
t.start()
