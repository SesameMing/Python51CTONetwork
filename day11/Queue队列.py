#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-15 23:04
import queue
# queue.Queue, 先进先出队列
# queue.LifoQueue, 先进后出队列
# queue.PriorityQueue, 优先级队列
# queue.deque, 双向队列

# 先进先出队列
# put放数据，是否阻塞，阻塞时的超时时间
# get去数据（默认阻塞）,是否阻塞，阻塞的超时事件
# 队列的最大长度
# qsize()真实个数
# maxsize 最大支持的个数
# join, task_done, 阻塞进程，当队列中那个任务执行完毕之后，不在阻塞

# q = queue.Queue(2)
# print(q.empty())
# q.put(11)
# q.put(22)
# print(q.empty())
# print(q.qsize())
# q.put(22)
# q.put(33, block=False)
# q.put(33, block=False, timeout=2)
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


q = queue.LifoQueue()
q.put(123)
q.put(456)
print(q.get())
print(q.get())
queue.PriorityQueue()