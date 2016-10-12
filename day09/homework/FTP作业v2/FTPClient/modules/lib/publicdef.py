#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-11 13:39
import os
import hashlib


def FileSize(path):
    """

    计算目录下的所有文件的大小

    """
    size = 0
    for root, dirs, files in os.walk(path, True):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        # 目录下文件大小累加
    return size


def getMD5(path):
    m = hashlib.md5()
    n = 1024*4
    inp = open(path, 'rb')
    while True:
        buf = inp.read(n)
        if buf:
            m.update(buf)
        else:
            break
    return m.hexdigest()