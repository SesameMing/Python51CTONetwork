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

