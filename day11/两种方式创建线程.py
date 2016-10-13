#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-13 17:51
import threading


def f1(arg):
    print(arg)

t = threading.Thread(target=f1, args=(123, ))
t.setDaemon(True)  # True 表示主线程不等此子线程
t.start()  # 不代表当前现成会被立即执行
t.join()  # 表示主线程到此，等待... 直到子线程执行完毕
# t.join(n)  # 参数 表示主线程在此最多等待n秒
f1(111)


class MyThread(threading.Thread):
    def run(self):
        print()


obj = MyThread()
obj.start()