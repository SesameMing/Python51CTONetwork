#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-18 19:56

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
ADMIN_DIR_FOLDER = os.path.join(BASE_DIR, 'db', 'admin')
USER_DIR_FOLDER = os.path.join(BASE_DIR, 'db', 'user')
SET_DIR_FILE = os.path.join(BASE_DIR, 'db', 'setting')


