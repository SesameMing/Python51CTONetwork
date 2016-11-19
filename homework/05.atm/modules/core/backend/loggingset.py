#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-21 14:24

import logging

def loger(logname):
    logger = logging.getLogger('test.log')
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fl = logging.FileHandler(logname, encoding='utf-8')
    fl.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')
    formatter_for_file = logging.Formatter('%(asctime)s - %(message)s')

    ch.setFormatter(formatter)
    fl.setFormatter(formatter_for_file)

    logger.addHandler(ch)
    logger.addHandler(fl)


    return logger

if __name__ == '__main__':

    mes = "111  透支取款"
    loger1 =loger('test.log')
    loger1.info('xxxxxx')
