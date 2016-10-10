#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:15
import os
import subprocess

class ftpserver():
    def __init__(self, now_path, his_path):
        self.now_path = now_path
        self.his_path = his_path

    def cd(self, obj, *args, **kwargs):
        """ 打开目录 """
        print(args[0]['recv_data']['path'])
        if args[0]['recv_data']['path'] == '.':
            if len(self.his_path) > 0:
                data = "dir %s" % (self.his_path.pop())
                p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
                send_data = p.stdout.read()
                send_data = str(send_data, encoding='gbk')
            else:
                send_data = "已经是最上层目录了"
        elif args[0]['recv_data']['path'] == '..':
            data = "dir %s" % (self.now_path)
            p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
            send_data = p.stdout.read()
            send_data = str(send_data, encoding='gbk')
        else:
            if len(self.his_path) > 0:
                self.his_path.append(self.now_path)
                self.now_path = os.path.join(self.now_path, args[0]['recv_data']['path'])
                data = "dir %s" % (self.now_path)
                p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
                send_data = p.stdout.read()
                send_data = str(send_data, encoding='gbk')
            else:
                send_data = "已经是最上层目录了"

        obj.request.sendall(bytes(send_data, encoding='utf8'))

    def put(self):
        """ 上传 """
        print('上传')

    def down(self, obj, *args, **kwargs):
        """ 下载 """
        print("下载")
        # readydate = "Ready|%s" %
        obj.request.sendall(bytes("下载", encoding='utf8'))