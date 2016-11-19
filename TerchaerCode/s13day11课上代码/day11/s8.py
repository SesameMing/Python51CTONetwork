#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from threading import Timer

def hello():
    print("hello, world")

t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed