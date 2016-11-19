#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
NUM = 10

def func(i,l):
    global NUM
    # 上锁
    l.acquire() # 30,5 25m5,20
    NUM -= 1
    time.sleep(2)
    print(NUM,i)
    # 开锁
    l.release()

# lock = threading.Lock()
# lock = threading.RLock()
lock = threading.BoundedSemaphore(5)

for i in range(30):
    t = threading.Thread(target=func,args=(i,lock,))
    t.start()
