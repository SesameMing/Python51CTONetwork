#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:15
# put F:\【学习中的项目】\Python\Python51CTONetwork\day09\homework\FTP作业\FTPClient\readme.md

import os
import re
import sys
import json
from modules.lib import publicdef
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
            filepath = args[0][1]
            filesize = os.path.getsize(filepath)
            filename = os.path.basename(filepath)
            filemd5 = publicdef.getMD5(filepath)
            send = {"action": "put", "filesize": filesize, "filename": filename, "filemd5": filemd5}
            obj.sendall(bytes(json.dumps(send), encoding='utf8'))

            # 接收服务器上是否存在该文件
            recv_data = obj.recv(1024).decode()
            if recv_data.startswith('czfile'):
                filewz = recv_data.split("|")[-1]
                choose = input("服务器存在该文件,是否续传<y/n>：").strip()
                if choose == 'y':
                    obj.sendall(bytes("xuchuan", encoding='utf8'))
                    xc_recv_data = obj.recv(1024).decode()
                    if xc_recv_data == "xcstart":
                        fo = open(filepath, 'rb')
                        fo.seek(int(filewz))
                        while True:
                            filedata = fo.read(1024)
                            if not filedata:
                                break
                            obj.sendall(filedata)
                        fo.close()
                        recv_data_s = obj.recv(1024).decode()
                        print(recv_data_s)
                else:
                    obj.sendall(bytes("start", encoding='utf8'))
                    recv_data = obj.recv(1024).decode()
            else:
                recv_data == "file"
                obj.sendall(bytes("start", encoding='utf8'))
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
            print("没找到要上传的文件")

    def down(self, obj, *args):
        """ 下载 """
        if os.path.exists(args[0][1]):
            choose = input("本地存在该文件,是否续传<y/n>：")
            if choose == 'y':
                loacl_file_size = os.path.getsize(args[0][1])
                send = {"action": "down", "filename": args[0][1], "moshi": "xc", "loacl_file_size": loacl_file_size}
                obj.sendall(bytes(json.dumps(send), encoding='utf8'))
                # 接收文件的大小
                recv_data = obj.recv(1024).decode()
                if recv_data.startswith('Ready'):
                    file_size = recv_data.split('|')[-1]
                    file_md5 = recv_data.split('|')[1]
                    obj.sendall(bytes('start', encoding='utf8'))
                    recv_file_size = 0
                    recv_file_data = b''
                    while recv_file_size < int(file_size):
                        recv_data = obj.recv(1024)
                        recv_file_data += recv_data
                        recv_file_size += len(recv_data)
                        # time.sleep(.1)  本机下载速度很快，所以可以使用 sleep来查看 进度条效果
                        sys.stdout.write('\r')
                        print("%.2f%%" % (recv_file_size / int(file_size) * 100), end='')
                        sys.stdout.flush()

                    fo = open(args[0][1], 'ab')
                    fo.write(recv_file_data)
                    fo.close()
                    down_file = publicdef.getMD5(args[0][1])
                    if file_md5 != down_file:
                        print("下载的文件和原文的文件的不一致")
                    else:
                        print("下载完成")
            else:
                send = {"action": "down", "filename": args[0][1], "moshi": "new"}
                obj.sendall(bytes(json.dumps(send), encoding='utf8'))
                # 接收文件的大小
                recv_data = obj.recv(1024).decode()
                if recv_data.startswith('Ready'):
                    file_size = recv_data.split('|')[-1]
                    file_md5 = recv_data.split('|')[1]
                    obj.sendall(bytes('start', encoding='utf8'))
                    recv_file_size = 0
                    recv_file_data = b''
                    while recv_file_size < int(file_size):
                        recv_data = obj.recv(1024)
                        recv_file_data += recv_data
                        recv_file_size += len(recv_data)
                        # time.sleep(.1)  本机下载速度很快，所以可以使用 sleep来查看 进度条效果
                        sys.stdout.write('\r')
                        print("%.2f%%" % (recv_file_size / int(file_size) * 100), end='')
                        sys.stdout.flush()

                    fo = open(args[0][1], 'wb')
                    fo.write(recv_file_data)
                    fo.close()
                    down_file = publicdef.getMD5(args[0][1])
                    if file_md5 != down_file:
                        print("下载的文件和原文的文件的不一致")
                    else:
                        print("下载完成")
        else:
            send = {"action": "down", "filename": args[0][1], "moshi": "new"}
            obj.sendall(bytes(json.dumps(send), encoding='utf8'))
            # 接收文件的大小
            recv_data = obj.recv(1024).decode()
            if recv_data.startswith('Ready'):
                file_size = recv_data.split('|')[-1]
                file_md5 = recv_data.split('|')[1]
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
                down_file = publicdef.getMD5(args[0][1])
                if file_md5 != down_file:
                    print("下载的文件和原文的文件的不一致")
                else:
                    print("下载完成")
        # else:
        #     print(recv_data)

    def mk(self, obj, *args):
        """ 创建目录 """
        send = {"action": "mk", "filename": args[0][1]}
        while re.search(r"[/:*?\\\"<>|]", send.get("filename")):
            send["filename"] = input("文件夹名称不正确，重新输入名称：")
        obj.sendall(bytes(json.dumps(send), encoding='utf8'))
        recv_data = obj.recv(1024).decode()
        print(recv_data)


