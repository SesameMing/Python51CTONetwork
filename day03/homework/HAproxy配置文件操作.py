#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-08-29 23:23

import os
CFG_FILE = "HAproxy.cfg"  # 配置文件名称
QUIT_CHAR = 'q'  # 退出字符
flag = True  # 循环标记


if os.path.exists(CFG_FILE):
    print("配置文件加载成功")
else:
    print("配置文件丢失。退出")
    exit(1)


def getinfo():
    """ 获取HAproxy配置信息 """
    pass


def addinfo():
    """ 添加HAproxy配置信息 """
    pass


def updateinfo():
    """ 修改HAproxy配置信息 """
    pass


def delinfo():
    """ 删除HAproxy配置信息 """
    pass


def bakupinfo():
    """ 备份HAproxy配置文件 """
    pass


def main():
    str = """
    ------------------------------------
    |  欢迎来到HAproxy管理脚本  v1.0.0 |
    ------------------------------------
    |    1.获取backend 和sever信息     |
    |    2.添加backend 和sever信息     |
    |    3.修改backend 和sever信息     |
    |    4.删除backend 和sever信息     |
    |    5.备份配置文件                |
    |    6.回滚配置文件                |
    ------------------------------------
    |   %s：退出         数字：选择     |
    ------------------------------------
    """ % QUIT_CHAR
    while flag:
        print(str)
        num = input("请输入您的选择：")
        if num.isdigit():
            pass
        else:
            pass

main()