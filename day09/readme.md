# 第9天

## TCP/IP
* 全称: transmission controll protocol and internet protocal
* tcp/ip协议是~~主机接入互联网以及接入互联网两台主机通信~~标准

## socket
1. python3.5的socket只能收发字节（2.7可以发送字符串）
2. 退出只在客户端退出就ok了
3. s.accprt() 和 s.recv() 是阻塞的（基于链路正常）
4. listen(n):n代表能挂起的连接数。（应该是能等待的把）
5. 服务端出现端口冲突：修改端口号
6. 