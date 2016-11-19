#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# import threading
# def f1(arg):
#    print(arg)

# t = threading.Thread(target=f1, args=(123,))
# t.start()
# t.run()
# run
import threading
class MyThread(threading.Thread):
   def __init__(self, func,args):
      self.func = func
      self.args = args
      super(MyThread, self).__init__()

   def run(self):
      self.func(self.args)

def f2(arg):
   print(arg)

obj = MyThread(f2,123)
obj.start()