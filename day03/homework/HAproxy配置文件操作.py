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
    domainList =[]
    print(" 获取backend 和sever信息 ")
    f = open(CFG_FILE, 'r+', encoding='utf-8')
    for i in f:
        if 'use_backend' not in i.strip():
            if 'backend' in i.strip():
                domainList.append(i.strip().split(" ")[1])
    f.close()
    for i in domainList:
        print(domainList.index(i), i)
    domain_num = input("请输入您要查看的那个域名序号：")
    if domain_num.isdigit():
        domain_int_num = int(domain_num)
        if domain_int_num < len(domainList):
            domain_1 = 'backend %s' % domainList[domain_int_num]
            with open(CFG_FILE, 'r+', encoding='utf-8') as f:
                for link in f:
                    print(link)


def addinfo():
    """ 添加HAproxy配置信息 """
    print(" 添加backend 和sever信息 ")


def updateinfo():
    """ 修改HAproxy配置信息 """
    print(" 修改backend 和sever信息 ")


def delinfo():
    """ 删除HAproxy配置信息 """
    print(" 删除backend 和sever信息 ")


def bakupinfo():
    """ 备份HAproxy配置文件 """
    print(" 备份配置文件 ")


def rollback():
    """ 回滚HAproxy配置文件 """
    print(" 回滚HAproxy配置文件 ")


str1 = """
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
    print(str1)
    num = input("请输入您的选择：")
    if num.isdigit():
        num_int = int(num)
        if num_int == 1:
            """ 获取backend 和sever信息 """
            getinfo()
        elif num_int == 2:
            """ 添加backend 和sever信息 """
            getinfo()

        elif num_int == 3:
            """ 修改backend 和sever信息 """
            updateinfo()
        elif num_int == 4:
            """ 删除backend 和sever信息 """
            delinfo()

        elif num_int == 5:
            """ 备份配置文件 """
            bakupinfo()

        elif num_int == 6:
            """ 回滚配置文件 """
            rollback()
        else:
            print("不正确的选项，请重新选择")
    else:
        if num == QUIT_CHAR:
            print("退出")
            flag = False

