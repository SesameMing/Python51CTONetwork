#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-23 20:23

import hashlib

obj = hashlib.md5()
obj.update(bytes('admin', encoding='utf-8'))
result = obj.hexdigest()
print(result)


# 加key密钥
obj = hashlib.md5(bytes('xxxxxxxx', encoding='utf-8'))
obj.update(bytes('admin', encoding='utf-8'))
result = obj.hexdigest()
print(result)