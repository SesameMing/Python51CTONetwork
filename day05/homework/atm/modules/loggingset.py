#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-21 14:24

import os
import logging
from conf import setting


def admin():
    logger = logging.getLogger(os.path.join(setting.ADMIN_DIR_FOLDER, 'log', 'admin.log'))
    logger.setLevel(logging.INFO)


