# 第10天
## 小知识
### 作用域
* python中无块级作用域
* python中以函数为作用域
* 函数体在没有执行之前，内部代码不执行

##
li = [x+100 for x in range(10)]
li = [x+100 for x in range(10) if x > 6 ]
li = [lambda:x for x in range(10)]
li[0]()输出的多少 （9）



## IO多路复用
### 概述
    select, poll, epoll

* 监听socket对象内部是否发生变化
* 什么时候变化？链接或收发消息
* 服务器端的socket对象发生变化-> 有新的链接来了
* sk：有新的链接来了...
* conn：要收“发”消息了
* IO多路复用 -- 监听socket对象内部是否发生变化？

实现读写分离

## 多线程、多进程
1. 一个应用程序，可以有多进程和多线程
2. 默认：单进程， 单线程
3. 单进程，多线程
  IO操作， 不占用CPU
    多线程提高并发
  计算性操作，占用cpu
    多进程提高并发
4. GIL，全局解释器锁

多线程/多进程 提供并发
IO密集型：多线程
计算密集型：多进程
  PS:IO操作不占用CPU； GIL,python有全局解释器锁
  
  

