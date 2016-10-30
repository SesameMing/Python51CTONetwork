#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 13:39
# Version：3.x
import redis


class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.199.213', port=6379)

    def public(self, msg, chan):
        self.__conn.publish(chan, msg)
        return True

    def subscribe(self, chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub