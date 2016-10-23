#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-23 20:00
import socket


# 验证主机是否存在
def yzhost(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.send(bytes('areyouready?'))
        recv = s.recv(1024).decode()
        s.close()
        if recv == 'yes':
            return True
        else:
            return False
    except:
        return False

# 验证主机权限（帐号密码）
def yzauth(ip, port, username, password):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.send(bytes('areyouready?'))
        recv = s.recv(1024).decode()
        s.close()
        if recv == 'yes':
            return True
        else:
            return False
    except:
        return False
