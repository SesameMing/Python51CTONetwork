#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import queue
# queue.Queue，先进先出队列
# queue.LifoQueue，后进先出队列
# queue.PriorityQueue，优先级队列
# queue.deque，双向对队

# q = queue.LifoQueue()
# q.put(123)
# q.put(456)
# print(q.get())

# q = queue.PriorityQueue()
# q.put((1,"alex1"))
# q.put((1,"alex2"))
# q.put((1,"alex3"))
# q.put((3,"alex3"))
# print(q.get())

# q = queue.deque()
# q.append(123)
# q.append(333)
# q.appendleft(456)
# q.pop()
# q.popleft()

# queue.Queue(2) 先进先出队列
# put放数据，是否阻塞，阻塞时的超时事件
# get取数据（默认阻塞）,是否阻塞，阻塞时的超时事件
# qsize()真实个数
# maxsize 最大支持的个数
# join,task_done，阻塞进程，当队列中任务执行完毕之后，不再阻塞

# q = queue.Queue(2)
# print(q.empty())
# q.put(11)
# q.put(22)
# print(q.empty())
# print(q.qsize())
# q.put(22)
# q.put(33, block=False)
# q.put(33,block=False, timeout=2)
# print(q.get())
# print(q.get())
# print(q.get(timeout=2))

# q = queue.Queue(5)
# q.put(123)
# q.put(456)
# q.get()
# q.task_done()
# q.get()
# q.task_done()
# q.join()

# q = queue.LifoQueue()
# # q.put(123)
# # q.put(456)
# # print(q.get())
# queue.PriorityQueue()