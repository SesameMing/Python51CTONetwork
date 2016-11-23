#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-22 15:48
# Version：3.x

import os


BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # 获取程序运行的入口目录层级
BD_FILE_PATH = os.path.join(BASE_PATH, 'config', 'db.conf')  # 获取数据库配置文件的路径
RB_FILE_PATH = os.path.join(BASE_PATH, 'config', 'rabbitMQ.conf')  # 获取rabbitMQ配置文件的路径
