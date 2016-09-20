#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-14 16:00


import time
import datetime


# time module
print(time.clock())  # 返回处理器时间 3.3开始废弃
print(time.process_time())  # 返回处理器时间 3.3开始废弃
print(time.time())  # 返回当前系统时间戳
print(time.ctime())  # 输出Wed Sep 14 16:16:10 2016, 当前系统时间
print(time.ctime(time.time()-86640))  # 将时间戳转为字符串格式
print(time.gmtime(time.time()-86640))  # 将时间戳转换struct_time格式
print(time.gmtime())
print(time.localtime())  # 将时间戳转换struct_time格式,但返回的是本地时间
print(time.mktime(time.localtime()))  # 与time.localtiem()功能想反，将struct_time格式转回时间戳格式
# time.sleep(4)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strptime("2016-09-14", "%Y-%m-%d"))
# datetime module
print(datetime.date.today())  # 输出格式2016-09-14
print(datetime.date.fromtimestamp(time.time()))  # 输出格式2016-09-14 时间戳转成日期
current_time = datetime.datetime.now()
print(current_time)  # 输出格式2016-09-14 17:53:24.499480
print(current_time.timetuple())  # 返回struct_time格式

print(current_time.replace(2014, 9, 12))   # 输出2014-09-12 18:17:20.264601 返回当前时间，但是指定值将被替换

str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(str_to_date)

print(datetime.datetime.now() + datetime.timedelta(days=10))  # 比现在加10天
print(datetime.datetime.now() + datetime.timedelta(days=-10))  # 比现在减10天
print(datetime.datetime.now() + datetime.timedelta(hours=10))  # 比现在加10小时
print(datetime.datetime.now() + datetime.timedelta(seconds=120))  # 比现在加120秒
