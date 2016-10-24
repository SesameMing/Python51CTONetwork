#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-23 20:00
import socket
import paramiko


# 验证主机是否能链接上
def ssh_host(ip, port, user, passwd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=int(port), username=user, password=passwd)
        ssh_session = client.get_transport().open_session()
        if ssh_session.active:
            client.close()
            return True
        else:
            return False
    except:
        return False


# 主机执行操作
def ssh_command(ip, port, user, passwd, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=int(port), username=user, password=passwd)
        ssh_session = client.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(command)
            return ssh_session.recv(1024).decode()
        else:
            return False
    except Exception as e:
        print(e)
        return False


class HostClent():
    def __init__(self, ip, port, user, passwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd

    # 链接主机并保留链接状态
    def ssh_host(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ip, port=int(self.port), username=self.user, password=self.passwd)
            ssh_session = client.get_transport().open_session()
            self.client = client
            self.ssh_session = ssh_session
            if ssh_session.active:
                return True
            else:
                return False
        except Exception as e:
            return False

    # 主机执行操作
    def ssh_command(self, command):
        ssh_session = self.client.get_transport().open_session()
        try:
            if ssh_session.active:
                ssh_session.exec_command(command)
                recv_data = b""
                while True:
                    data = ssh_session.recv(1024)
                    if not data:
                        break
                    else:
                        recv_data += data
                return recv_data.decode()
            else:
                return False
        except Exception as e:
            return False
