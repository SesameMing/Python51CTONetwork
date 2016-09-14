#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-14 14:10

import json
import requests

url = "http://wthrcdn.etouch.cn/weather_mini?city=上海"
response = requests.get(url)
response.encoding = "utf-8"
requests_dic = json.loads(response.text)
print(requests_dic)
