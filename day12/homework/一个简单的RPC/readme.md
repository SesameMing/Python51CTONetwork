http://t.51cto.com/exam/view?id=1027
# 一个简单的RPC（远程调用模型）
1. server端将要执行的命令及参数发送到RabbitMQ，
2. client端从RabbitMQ获取要执行的命令，命令执行完成之后，将结果返回给server端
3. server端接受client端的命令执行结果，并处理，
4. 可选择指定主机或者主机组


## 00 前提
需要另外安装`sqlalchemy_utils` 用来验证数据库是否存在

## 01运行
### 服务器端
首先Server/server.py中的第12行,13行

```
rabbitMQhost = '192.168.199.213'  # rabbitMQ主机地址
severities = ['192.168.199.213']  # 本机ip
```

将设置为自己服务器对应的配置。

然后执行Server/server.py

### 客户端
执行Client/Client.py
* 先设置数据库配置
* 设置登录帐号密码
* 设置RabbitMQ服务器地址
* 添加分组
* 添加主机
* 下发指令

## 02 文件介绍
Client
* client.py 主程序入口
* Client/bin/lib/mysql_table.py 是sqlalchemy相关操作
* Client/bin/lib/rabbit_mq.py 是rabbitMQ相关操作
* Client/config/db.conf 是数据库配置文件
* Client/config/rabbitMQ.conf 是rabbitMQ配置文件

## 03 初始化
删除Client/config/下的db.conf和rabbitMQ.conf 初始化 客户端操作。
