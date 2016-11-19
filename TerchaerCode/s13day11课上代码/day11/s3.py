#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import queue
import threading
import time
q = queue.Queue()

def productor(arg):
    """
    买票
    :param arg:
    :return:
    """
    q.put(str(arg) + '- 包子')


for i in range(300):
    t = threading.Thread(target=productor,args=(i,))
    t.start()

def consumer(arg):
    """
    服务器后台
    :param arg:
    :return:
    """
    while True:
        print(arg, q.get())
        time.sleep(2)

for j in range(3):
    t = threading.Thread(target=consumer,args=(j,))
    t.start()