#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-06 15:52
import re
import hashlib
import socket
import json
from modules.lib import ftpserver
ip_port = ()


def login(s):
    username = input("请输入用户名：").strip()
    while not username:
        username = input("用户名不能为空：").strip()
    password = input("请输入密码：").strip()
    while not password:
        password = input("密码不能为空：").strip()
    obj = hashlib.md5()
    obj.update(bytes(password, encoding='utf-8'))
    password = obj.hexdigest()
    user = {'username': username, 'password': password}
    yz_send = json.dumps(user)
    s.send(bytes(yz_send, encoding='utf8'))
    yz_data = s.recv(1024).decode()
    if yz_data.startswith('error'):
        print(yz_data.split("|")[-1])
        print("请重新输入")
        login(s)
    else:
        return True

def ConnetServer():
    """
    链接服务器
    :return: socket对象
    """
    print("欢迎使用FTPv1.0")
    ip = input("请输入服务端ip地址：").strip()
    while not re.match(r"^\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*$", ip):
        ip = input("ip地址不符合规范,请重新输入：")
    port = input("请输入服务端端口：").strip()
    while not re.match(r"[0-9]{1,4}$", port):
        port = input("服务端端口不符合规范,请重新输入：").strip()

    s = socket.socket()
    ip_port = (ip, int(port))
    try:
        s.connect(ip_port)
        print("服务器链接成功")
        return s
    except Exception as e:
        print("登录超时，检查ip地址以及端口号是否有误")
        ConnetServer()


def main():
    s = ConnetServer()
    recv_data = s.recv(1024).decode()
    print(recv_data)
    login(s)
    confirm_data = 'successdir'
    s.send(bytes(confirm_data, encoding='utf8'))
    str1 = s.recv(1024).decode()
    print(str1)

    obj = ftpserver.ftpserver()
    while True:
        inp_data = input(">>>:").strip()
        int_data = inp_data.split(' ')
        if len(int_data) >= 2:
            if hasattr(obj, int_data[0]):
                func = getattr(obj, int_data[0])
                func(s, int_data)
            else:
                print("不存在的方法")
        else:
            print_str = """【操作命令】
cd dirname: 打开目录
put fliename[path/fliename] :上传文件
down fliename : 下载文件

本层目录: cd .
上层目录: cd ..
开打目录：cd dirname
创建目录: mk dirname"""
            print(print_str)
            print("错误的指令，请重新输入")


def login2():
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
    # str = "我的撒网的爱的 阿萨达 /单位安慰阿萨达"
    # print(re.search(r"[/:*?\\\"<>|]", str))
    main()