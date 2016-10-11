#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:15
import os
import sys
import json
import subprocess
from modules.lib import publicdef
from conf import setting

class ftpserver():
    def __init__(self, home_path, now_path, his_path, name):
        self.home_path = home_path
        self.now_path = now_path
        self.his_path = his_path
        self.name = name

    def cd(self, obj, *args, **kwargs):
        """ 打开目录 """
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

            self.his_path.append(self.now_path)
            self.now_path = os.path.join(self.now_path, args[0]['recv_data']['path'])
            data = "dir %s" % (self.now_path)
            p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
            send_data = p.stdout.read()
            send_data = str(send_data, encoding='gbk')


        obj.request.sendall(bytes(send_data, encoding='utf8'))

    def put(self, obj, *args, **kwargs):
        """ 上传 """
        file_size = int(args[0]['recv_data']['filesize'])
        userconf = json.load(open(os.path.join(setting.USER_CONFIG_DIR, self.name, 'user.config'), 'r'))
        # 判断 用户上传加上原本内容是否超额

        if int(userconf.get('storesizi'))*1024*1024 >= int(publicdef.FileSize(self.home_path)) + int(file_size):
            if file_size > 0:
                obj.request.sendall(bytes("start", encoding='utf8'))
                recv_file_size = 0
                recv_file_data = b''
                while recv_file_size < file_size:
                    recv_data = obj.request.recv(1024)
                    recv_file_data += recv_data
                    recv_file_size += len(recv_data)
                    # 进度条
                    sys.stdout.write('\r')
                    print("%.2f%%" % (recv_file_size / int(file_size) * 100), end='')
                    sys.stdout.flush()

                fo = open(os.path.join(self.now_path, args[0]['recv_data']['filename']), 'wb')
                fo.write(recv_file_data)
                fo.close()
            print("上传了文件 %s" % args[0]['recv_data']['filename'])
            obj.request.sendall(bytes("上传成功", encoding='utf8'))
        else:
            print("您的存储不够")
            obj.request.sendall(bytes("您的存储不够, 不能上传了", encoding='utf8'))

    def down(self, obj, *args, **kwargs):
        """ 下载 """
        if os.path.isfile(os.path.join(self.now_path, args[0]['recv_data']['filename'])):
            readydate = "Ready|%s" % os.path.getsize(os.path.join(self.now_path, args[0]['recv_data']['filename']))
            obj.request.sendall(bytes(readydate, encoding='utf8'))
            racv_ready = obj.request.recv(1024)
            if racv_ready.decode() == 'start':
                fo = open(os.path.join(self.now_path, args[0]['recv_data']['filename']), 'rb')
                while True:
                    filedata = fo.read(1024)
                    if not filedata:
                        break
                    obj.request.sendall(filedata)
                fo.close()
                print("发送文件完毕")
        else:
            obj.request.sendall(bytes("下载的文件不存在，或者不是文件,暂时不支持下载文件夹", encoding='utf8'))