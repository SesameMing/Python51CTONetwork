#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-20 13:09

import memcache

mc = memcache.Client(['192.168.199.213:12000'], debug=True)
mc.set("foo", "bar")
ret = mc.get("foo")
print(ret)