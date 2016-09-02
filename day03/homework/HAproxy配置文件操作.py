#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-08-29 23:23

import os
import shutil
CFG_FILE = "HAproxy.cfg"  # 配置文件名称
CFG_FILE_BAK = "HAproxy.cfg.bak"
QUIT_CHAR = 'q'  # 退出字符
flag = True  # 循环标记


if os.path.exists(CFG_FILE):
    print("配置文件加载成功")
else:
    print("配置文件丢失。退出")
    exit(1)


def getdominlist():
    """ 获取配置信息中的域名列表 """
    domainList = []
    f = open(CFG_FILE, 'r+', encoding='utf-8')
    for i in f:
        if i.strip().startswith("backend"):
            domainList.append(i.strip().split(" ")[1])
    f.close()
    return domainList


def getinfo():
    """ 获取HAproxy配置信息 """
    domainList = getdominlist()
    for i in domainList:
        print(domainList.index(i), i)
    domain_num = input("请输入您要查看的那个域名序号：")
    if domain_num.isdigit():
        domain_int_num = int(domain_num)
        if domain_int_num < len(domainList):
            domain_1 = 'backend %s' % domainList[domain_int_num]
            with open(CFG_FILE, 'r+', encoding='utf-8') as f:
                flag = False
                for i in f:
                    if i.strip().startswith("backend") and i.strip() == domain_1:
                        flag = True
                        continue
                    if flag and i.strip().startswith("backend"):
                        flag = False
                        break
                    if flag and i.strip():
                        print(i.strip())
        else:
            print("输入的序号不正确")
    else:
        pass


def addinfo():
    """ 添加HAproxy配置信息 """
    print("添加backend 和sever信息")
    domainList = getdominlist()
    inputBackend = input("请输入的您要添加的Backend：")
    inputserver = input("请输入server信息：")
    if inputBackend not in domainList:
        """ backend 不在原配置文件中 """
        with open(CFG_FILE, 'r') as old , open(CFG_FILE_BAK, 'w') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + inputBackend + "\n")
            new.write(" " * 8 + inputserver + "\n")
    else:
        pass




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
            addinfo()

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

