#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-17 18:51
import threading
import time

NUM = 30


def func(i, l):
    global NUM
    l.acquire()
    NUM -= 1
    time.sleep(1)
    print(NUM, i)
    l.release()

# look = threading.Lock()
# look = threading.RLock()
look = threading.BoundedSemaphore(5)


for i in range(30):
    t = threading.Thread(target=func, args=(i, look))
    t.start()