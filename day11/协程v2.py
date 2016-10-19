#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-19 11:56

import gevent
import requests


def f(url):
    print('GET:%s ' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received form %s . ' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.baidu.com/'),
    gevent.spawn(f, 'http://www.qq.com/'),
    gevent.spawn(f, 'https://github.com/'),
                ])
