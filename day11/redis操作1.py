#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-20 15:00

import redis

r = redis.Redis(host='192.168.199.213', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))
