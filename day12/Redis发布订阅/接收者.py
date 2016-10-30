#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 14:09
# Version：3.x

import RedisHelper

obj = RedisHelper.RedisHelper()
data = obj.subscribe('fm1117.7')
print(data.parse_response())