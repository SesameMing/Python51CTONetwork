#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-22 20:47

# 设置每天0.点指定执行。 每个月10号自动统计透支，并从余额中扣除

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.core import crontab as src_crontab

if __name__ == '__main__':
    src_crontab.run()