#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-25 18:52
import zipfile

f = zipfile.ZipFile('text.zip', 'w')
f.write('oooo.xml')
f.write('readme.md')
f.close()


