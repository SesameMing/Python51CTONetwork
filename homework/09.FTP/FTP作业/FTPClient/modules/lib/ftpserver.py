#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:15
# put F:\【学习中的项目】\Python\Python51CTONetwork\day09\homework\FTP作业\FTPClient\readme.md

import os
import sys
import json

import time


class ftpserver():

    def cd(self, obj, *args):
        """ 打开目录 """
        send = {"action": "cd", "path": args[0][1]}
        obj.sendall(bytes(json.dumps(send), encoding='utf8'))
        recv_data = obj.recv(1024).decode()
        print(recv_data)

    def put(self, obj, *args):
        """ 上传 """
        # 判断上传的是不是文件
        if os.path.isfile(args[0][1]):

            # 判断输入的路径是绝对路径还是相对路径,不是绝对路径，就组装成绝对路径。
            # 后来发现,相对路径也是可以的，判断文件大小的时候用错了函数
            # if not os.path.isabs(args[0][1]):
            #     filepath = os.path.join(os.getcwd(), args[0][1])
            #     print(filepath)
            # else:
            #     filepath = args[0][1]

            filepath = args[0][1]
            filesize = os.path.getsize(filepath)
            filename = os.path.basename(filepath)
            send = {"action": "put", "filesize": filesize, "filename": filename}
            obj.sendall(bytes(json.dumps(send), encoding='utf8'))
            recv_data = obj.recv(1024).decode()
            if recv_data == 'start':
                fo = open(filepath, 'rb')
                while True:
                    filedata = fo.read(1024)
                    if not filedata:
                        break
                    obj.sendall(filedata)
                fo.close()
                recv_data = obj.recv(1024).decode()
                print(recv_data)
            else:
                print(recv_data)

        else:
            print("没找到要上传的文件")

    def down(self, obj, *args):
        """ 下载 """
        send = {"action": "down", "filename": args[0][1]}
        obj.sendall(bytes(json.dumps(send), encoding='utf8'))
        # 接收文件的大小
        recv_data = obj.recv(1024).decode()
        if recv_data.startswith('Ready'):
            file_size = recv_data.split('|')[-1]
            obj.sendall(bytes('start', encoding='utf8'))
            recv_file_size = 0
            recv_file_data = b''
            while recv_file_size < int(file_size):
                recv_data = obj.recv(1024)
                recv_file_data += recv_data
                recv_file_size += len(recv_data)
                # time.sleep(.1)  本机下载速度很快，所以可以使用 sleep来查看 进度条效果
                sys.stdout.write('\r')
                print("%.2f%%" % (recv_file_size/int(file_size)*100), end='')
                sys.stdout.flush()

            fo = open(args[0][1], 'wb')
            fo.write(recv_file_data)
            fo.close()
            print("下载完成")

        else:
            print(recv_data)



