#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import sys,time
def view_bar(total,start=0):
    while start < int(total):
        start += 1                                          #1可以替换为每次接收数据的大小
        c = int((start / int(total)) * 70)                  #当前需要打印的#的数量
        p = float((start / int(total)))                     #当前传输完毕的数据百分比
        j = "#" * c
        sys.stdout.write("[{: <70s}]{:.0%}\r".format(j,p))
        time.sleep(0.1)
    print('')
view_bar(100)