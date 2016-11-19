#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import threading

def func(i,e):
    print(i)
    e.wait() # 检测是什么等，如果是红灯，停；绿灯，行
    print(i+100)

event = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(i,event,))
    t.start()
#========
event.clear() # 设置成红灯
inp = input('>>>')
if inp == "1":
    event.set() # 设置成绿灯
