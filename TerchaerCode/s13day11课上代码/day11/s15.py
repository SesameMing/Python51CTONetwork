#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from multiprocessing import Process
from multiprocessing import queues
from multiprocessing import Array
from multiprocessing import RLock, Lock, Event, Condition, Semaphore
import multiprocessing
import time

def foo(i,lis):
    lis[0] = lis[0] - 1
    time.sleep(1)

    print('say hi',lis[0])

if __name__ == "__main__":
    # li = []
    li = Array('i', 1)
    li[0] = 10
    for i in range(10):
        p = Process(target=foo,args=(i,li))
        p.start()