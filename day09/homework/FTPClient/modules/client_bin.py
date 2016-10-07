#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-06 15:52
import re
import hashlib
import socket
import json
ip_port = ()

def main(ip_port, user):
    s = socket.socket()
    s.connect(ip_port)
    yz_send = json.dumps(user)
    s.send(bytes(yz_send, encoding='utf8'))
    yz_data = s.recv(1024).decode()
    print(yz_data)
    input(">>>:")


def login():
    print("欢迎使用FTPv1.0")
    ip = input("请输入服务端ip地址：").strip()
    while not re.match(r"^\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*$", ip):
        ip = input("ip地址不符合规范,请重新输入：")
    port = input("请输入服务端端口：").strip()
    while not re.match(r"[0-9]{1,4}$", port):
        port = input("服务端端口不符合规范,请重新输入：").strip()
    username = input("请输入用户名：").strip()
    while not username:
        username = input("用户名不能为空：").strip()
    password = input("请输入密码：").strip()
    while not password:
        password = input("密码不能为空：").strip()

    obj = hashlib.md5()
    obj.update(bytes(password, encoding='utf-8'))
    password = obj.hexdigest()
    ip_port = (ip, int(port))
    user = {'username': username, 'password': password}

    main(ip_port, user)


def run():
    login()