#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:39

import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVER_CONFIG_DIR = os.path.join(BASE_PATH, 'db', 'server')
USER_CONFIG_DIR = os.path.join(BASE_PATH, 'db', 'user')
USER_HOME_DIR = os.path.join(BASE_PATH, 'home', 'user')
