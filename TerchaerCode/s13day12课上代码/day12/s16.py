# Author:Alex Li
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s13')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select * from t10")

# 获取第一行数据
# row_1 = cursor.fetchone()

# 获取前n行数据
# row_2 = cursor.fetchmany(3)
# 获取所有数据
row_3 = cursor.fetchall()
print(row_3)
cursor.scroll(-2,mode='relative')
row_3 = cursor.fetchall()
print(row_3)

conn.commit()
cursor.close()
conn.close()