#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-17 18:51
import threading
import time

NUM = 10


def func(l):
    global NUM
    l.acquire()
    NUM -= 1
    time.sleep(1)
    print(NUM)
    l.release()



look = threading.Lock()
look = threading.RLock()

for i in range(10):
    t = threading.Thread(target=func, args=(look,))
    t.start()