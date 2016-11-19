#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import time
def f1(arg, t=None):
    if t:
        t._delete()
    time.sleep(5)
    print(arg)


# for i in range(10):
#     f1(i)
# 单进程、单线程的应用程序
import threading
t1 = threading.Thread(target=f1, args=(1,))
#t.setDaemon(True) # true，表示主线程不等此子线程
t1.start()# 不代表当前线程会被立即执行
#t.join(2)          # 表示主线程到此，等待 ... 直到子线程执行完毕
                   # 参数，表示主线程在此最多等待n秒

t2 = threading.Thread(target=f1, args=(2,t1))
t2.start()# 不代表当前线程会被立即执行
print('end')
print('end')
print('end')
print('end')
print('end')