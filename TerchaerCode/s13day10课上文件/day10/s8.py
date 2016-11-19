#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import time
def f1(i):
    time.sleep(1)
    print(i)

import threading
for j in range(10):
    t1 = threading.Thread(target=f1, args=(j,))
    t1.start()
