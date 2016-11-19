#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

# print(__file__)

import sys
import time


def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r1 = '\r%s>%d%%' %("="*num, rate_num)
    sys.stdout.write(r1)
    sys.stdout.flush()


if __name__ == '__main__':
    # r = ' %d%%' % (1, )
    # print(r)
    # 0 - 100
    for i in range(0, 101):
        time.sleep(0.1)
        view_bar(i, 100)