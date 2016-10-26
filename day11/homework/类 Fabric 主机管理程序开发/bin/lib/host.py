#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-23 20:00
import socket
import paramiko

class HostClent():
    def __init__(self, ip, port, user, passwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.nowpath = ""

    # 链接主机并保留链接状态
    def ssh_host(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ip, port=int(self.port), username=self.user, password=self.passwd)
            ssh_session = client.get_transport().open_session()
            if ssh_session.active:
                ssh_session.exec_command('pwd')
                data = ssh_session.recv(1024).decode
                self.nowpath = data
                return True
            else:
                return False
        except Exception as e:
            return False

    # 主机执行操作
    def ssh_command(self, command):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.ip, port=int(self.port), username=self.user, password=self.passwd)
        ssh_session = client.get_transport().open_session()
        # ssh_session = self.client.get_transport().open_session()
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
                print("[%s]".center(50, "-") % self.ip)
                print(recv_data.decode())
            else:
                return False
        except Exception as e:
            return False

    # 上传
    def put(self, inp):
        try:
            transport = paramiko.Transport((self.ip, int(self.port)))
            transport.connect(username=self.user, password=self.passwd)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(inp.split()[1], inp.split()[2])
            transport.close()
            print("\033[32;0m【%s】 上传 文件【%s】 成功....\033[0m" % (self.ip, inp.split()[2]))
        except Exception as error:  # 抓住异常
            print("\033[31;0m错误:【%s】【%s】\033[0m" % (self.ip, error))

    def run(self, cmd):
        cmd_str = cmd.split()[0]
        if hasattr(self, cmd_str):
            func = getattr(self, cmd_str)
            func(cmd)
        else:
            self.ssh_command(cmd)


