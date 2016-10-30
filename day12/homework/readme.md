http://t.51cto.com/exam/view?id=1027
# 一个简单的RPC（远程调用模型）
1. server端将要执行的命令及参数发送到RabbitMQ，
2. client端从RabbitMQ获取要执行的命令，命令执行完成之后，将结果返回给server端
3. server端接受client端的命令执行结果，并处理，
4. 可选择指定主机或者主机组