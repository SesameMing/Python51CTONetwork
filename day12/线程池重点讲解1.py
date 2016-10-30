#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 10:08
import contextlib


@contextlib.contextmanager
def worker_state(state_list, worker_thread):
    print('start')
    state_list.append(worker_thread)
    try:
        yield
    finally:
        state_list.remove(worker_thread)
        print('end')

free_list = []
current_thread = 'alex'
with worker_state(free_list, current_thread):
    print(123)
    print(456)
