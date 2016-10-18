#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-18 9:59

import queue
import threading
import time


class ThreadPool:
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self._q = queue.Queue(maxsize)
        for i in range(maxsize):
            self._q.put(threading.Thread)

    def get_thread(self):
        return self._q.get()

    def add_thread(self):
        self._q.put(threading.Thread)

pool = ThreadPool(5)


def task(arg, p):
    print(arg)
    time.sleep(1)
    p.add_thread()

for i in range(100):
    t = pool.get_thread()
    obj = t(target=task, args=(i, pool, ))
    obj.start()

