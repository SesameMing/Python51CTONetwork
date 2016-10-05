#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-28 11:57
import os
import logging


class loger:
    def __init__(self):
        self.logpath = 'log/runtime.log'

    def log(self):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 记录到文件
        fh = logging.FileHandler(self.getLoginpath(), encoding='utf-8')
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('[系统信息]：%(message)s')
        formatter_for_file = logging.Formatter('%(asctime)s - %(message)s')

        ch.setFormatter(formatter)
        fh.setFormatter(formatter_for_file)
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger

    def log2(self):
        # 创建一个logger
        logger = logging.getLogger('test.log')
        logger.setLevel(logging.DEBUG)

        # 记录到文件
        fh = logging.FileHandler(self.getLoginpath(), encoding='utf-8')
        fh.setLevel(logging.INFO)
        formatter_for_file = logging.Formatter('%(asctime)s - %(message)s')
        fh.setFormatter(formatter_for_file)
        logger.addHandler(fh)
        return logger

    def setLoginpath(self, logpath):
        self.logpath = logpath

    def getLoginpath(self):
        return self.logpath



if __name__ == '__main__':
    r = loger()
    r.info('xxxxxx')