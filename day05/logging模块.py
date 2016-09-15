#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-14 18:37
import logging
# 打印输出日志
# logging.warning("user [alex] attempted wrong password more then 4 times")
# logging.critical("server is down")

# 将级别高于等于info的 写入日志文件
# logging.basicConfig(filename='example.log', level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, to')


logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, to')