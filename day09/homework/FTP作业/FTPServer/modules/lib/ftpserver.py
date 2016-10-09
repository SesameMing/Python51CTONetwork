#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-06 0:15

class ftpserver():

    def cd(self, obj, *args, **kwargs):
        """ 打开目录 """
        obj.request.sendall(bytes("打开目录", encoding='utf8'))

    def put(self):
        """ 上传 """
        print('上传')

    def down(self):
        """ 下载 """
        print("下载")
