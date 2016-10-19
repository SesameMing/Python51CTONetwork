#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-19 11:56

import gevent


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo ageni')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit contenxt switch back to bar')

gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])