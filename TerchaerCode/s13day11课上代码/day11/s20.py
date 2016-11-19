#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import memcache

import memcache
mc = memcache.Client(['192.168.11.145:12001'], debug=True, cache_cas=True)
# mc.servers

v = mc.gets('product_count')
print(v)
mc.cas('product_count', "111")
# ...
# 如果有人在gets之后和cas之前修改了product_count，那么，下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生
mc.cas('product_count', "899")