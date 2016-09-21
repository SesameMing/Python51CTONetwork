#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-21 14:59
# 用户登录客户端

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.core import atm_client_mian as client
client.run()