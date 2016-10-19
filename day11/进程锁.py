#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-19 11:25

from multiprocessing import Pool
import time


def f1(arg):
    time.sleep(1)
    print(arg)

if __name__ == '__main__':
    pool = Pool(5)

    for i in range(30):
        # pool.apply(func=f1, args=(i,))
        pool.apply_async(func=f1, args=(i,))  # 异步执行多线程

    # pool.close()  # 所有的任务执行完毕
    # time.sleep(1)
    # pool.terminate()  # 立即终止
    # pool.join()
