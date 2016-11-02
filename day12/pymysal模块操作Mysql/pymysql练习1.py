#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-01 15:47
# Version：3.x

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test')
cursor = conn.cursor()
cursor.execute("select * from t")

row_1 = cursor.fetchone()
print(row_1)

conn.commit()
cursor.close()
conn.close()