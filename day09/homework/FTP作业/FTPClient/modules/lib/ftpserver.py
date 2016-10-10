#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:15
import json
class ftpserver():

    def cd(self, obj, *args):
        """ 打开目录 """
        send = {"action": "cd", "path": args[0][1]}
        obj.sendall(bytes(json.dumps(send), encoding='utf8'))
        recv_data = obj.recv(1024).decode()
        print(recv_data)

    def put(self):
        """ 上传 """
        print('上传')

    def down(self, obj, *args):
        """ 下载 """
        send = {"action": "down", "filename": args[0][1]}
        obj.sendall(bytes(json.dumps(send), encoding='utf8'))
        # 接收文件的大小
        recv_data = obj.recv(1024).decode()
        print(recv_data)


