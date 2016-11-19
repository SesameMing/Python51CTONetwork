# Author:Alex Li
import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.11.87')

    def publish(self, msg, chan):
        self.__conn.publish(chan, msg)
        return True

    def subscribe(self, chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub

