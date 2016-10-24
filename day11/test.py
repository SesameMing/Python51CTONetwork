#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-24 11:09

import paramiko

def main():
    host = "218.244.139.110"
    port = 22
    user = "root"
    pswd = "C02dbb9e"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pswd)
    stdin, stdout, stderr = ssh.exec_command('pwd')
    print(stdout.read().decode())
    ssh.close()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
