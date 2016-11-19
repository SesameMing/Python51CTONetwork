#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from multiprocessing import Pool
import time
def f1(arg):
    print(arg,'b')
    time.sleep(5)
    print(arg,'a')
if __name__ == "__main__":
    pool = Pool(5)

    for i in range(30):
        # pool.apply(func=f1,args=(i,))
        pool.apply_async(func=f1,args=(i,))

    # pool.close() # 所有的任务执行完毕
    time.sleep(2)
    pool.terminate() # 立即终止
    pool.join()
    pass