# FTP 作业

http://t.51cto.com/exam/view?id=1024


FTP：
1. 用户登陆
2. 上传/下载文件
3. 不同用户家目录不同
4. 用户登陆server后，可切换目录
5. 查看当前目录下文件


* FTPServer FTP的服务端
* FTPClient FTP的客户端


## 运行
首先运行 FTP的服务端的 server.py
   1.启动FTPServer 
   2.修改FTPServer端口 
   3.查看用户
   4.添加用户 
   5.修改用户 
   6.删除用户以及用户目录
   
先启动FTPServer 

运行 FTP的客户端 
输入 FTPServer服务端启动时 出现的服务端ip 和 端口号（暂时不支持类linux系统,用python3没获取到网卡的ip地址）
默认帐号：daming
默认密码：111

【操作命令】
cd dirname: 打开目录
put fliename[path/fliename] :上传文件
down fliename : 下载文件

本层目录: cd .
上层目录: cd ..
开打目录：cd dirname
创建目录: mk dirname