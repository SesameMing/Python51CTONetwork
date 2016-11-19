#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-28 11:57
import os
import logging


def log():
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[系统信息]：%(message)s')

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger



