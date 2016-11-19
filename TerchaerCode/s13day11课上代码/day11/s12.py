#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from multiprocessing import Process
from multiprocessing import queues
import multiprocessing
from multiprocessing import Array

def foo(i,arg):
    # arg.put(i)
    # print('say hi',i,arg.qsize())
    arg[i] = i + 100
    for item in arg:
        print(item)
    print('================')

if __name__ == "__main__":
    # li = []
    # li = queues.Queue(20,ctx=multiprocessing)
    li = Array('i', 10)
    for i in range(10):
        p = Process(target=foo,args=(i,li,))
        #p.daemon = True
        p.start()
        #p.join()
