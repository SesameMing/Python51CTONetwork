#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-08-29 23:23
import os
import shutil
CFG_FILE = "HAproxy.cfg"            # 配置文件名称
CFG_FILE_BAK = "HAproxy.cfg.bak"    # 备份配置文件名称
CFG_FILE_TEMP = "HAproxy.cfg.temp"  # 临时配置文件名称
QUIT_CHAR = 'q'                     # 退出字符
flag = True                         # 循环标记·

# 检查配置文件是否存在
if os.path.exists(CFG_FILE):
    print("配置文件加载成功")
else:
    print("配置文件丢失。退出")
    exit(1)


# 备份文件，并生成新的配置文件
def filecopy():
    shutil.copy(CFG_FILE, CFG_FILE_BAK)
    shutil.copy(CFG_FILE_TEMP, CFG_FILE)


# 获取配置文件中的backend列表
def getdominlist():
    """ 获取配置信息中的域名列表 """
    domainList = []
    f = open(CFG_FILE, 'r+', encoding='utf-8')
    for i in f:
        if i.strip().startswith("backend"):
            domainList.append(i.strip().split(" ")[1])
    f.close()
    return domainList

# 获取对应backend的server列表
def getserver(backend):
    server = []
    domain_1 = 'backend %s' % backend
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
                server.append(i.strip())
    return server


# 获取HAproxy配置信息
def getinfo():
    """ 获取HAproxy配置信息 """
    domainList = getdominlist()
    for i in domainList:
        print(domainList.index(i), i)
    domain_num = input("请输入您要查看的那个域名序号：")
    if domain_num.isdigit():
        domain_int_num = int(domain_num)
        if domain_int_num < len(domainList):
            server = getserver(domainList[domain_int_num])
            for i in server:
                print(i)
        else:
            print("输入的序号不正确")
    else:
        print("输入的序号不正确")


# 添加HAproxy配置信息
def addinfo():
    """ 添加HAproxy配置信息 """
    print("添加backend 和sever信息")
    domainList = getdominlist()
    inputBackend = input("请输入的您要添加的Backend：")
    serverip = input("输入新的serverip值：")
    weight = input("输入新的weight值：")
    maxconn = input("输入新的maxconn值：")
    inputserver = """        server %s %s weight %s maxconn %s\n""" % (serverip, serverip, weight, maxconn)
    if inputBackend not in domainList:
        """ backend 不在原配置文件中 """
        with open(CFG_FILE, 'r') as old, open(CFG_FILE_TEMP, 'w', encoding='utf-8') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + inputBackend + "\n")
            new.write(inputserver)
        filecopy()
        print("添加数据成功")
    else:
        server = getserver(inputBackend)
        if inputserver.strip() in server:
            print("您要添加的数据已经存在")
        else:
            server.append(inputserver.strip())
            with open(CFG_FILE, 'r') as old, open(CFG_FILE_TEMP, 'w', encoding='utf-8') as new:
                flag = False
                for line in old:
                    if line.strip().startswith('backend') and line.strip() == 'backend '+inputBackend:
                        flag = True
                        new.write(line)
                        for new_server in server:
                            new.write(" "*8 + new_server + "\n")
                            print(new_server)
                        continue
                    elif flag and line.strip().startswith('backend'):
                        flag = False
                        new.write(line)
                        continue
                    elif line.strip() and not flag:
                        new.write(line)
            filecopy()
            print("添加数据成功")


# 修改HAproxy配置信息
def updateinfo():
    """修改HAproxy配置信息 """
    print("修改backend 和sever信息 ")
    domainList = getdominlist()
    for i in domainList:
        print(domainList.index(i), i)
    domain_num = input("请输入您要修改的那个域名序号：")
    if domain_num.isdigit():
        domain_int_num = int(domain_num)
        if domain_int_num < len(domainList):
            server = getserver(domainList[domain_int_num])
            for i in server:
                print(server.index(i), i)
            server_num= input("选择您要修改的server信息:")
            if server_num.isdigit():
                server_int_num = int(server_num)
                if server_int_num < len(server):
                    serverip = input("输入新的serverip值：")
                    weight = input("输入新的weight值：")
                    maxconn = input("输入新的maxconn值：")
                    upserverdate = """        server %s %s weight %s maxconn %s\n""" % (serverip, serverip, weight, maxconn)
                    with open(CFG_FILE, 'r') as old, open(CFG_FILE_TEMP, 'w', encoding='utf-8') as new:
                        flag = False
                        for line in old:
                            if line.strip().startswith('backend') and line.strip() == 'backend ' + domainList[domain_int_num]:
                                flag = True
                                new.write(line)
                                for server_link in server:
                                    if server_link == server[server_int_num]:
                                        new.write(upserverdate)
                                    else:
                                        new.write(" " * 8 + server_link + "\n")
                            elif flag and line.strip().startswith('backend'):
                                flag = False
                                new.write(line)
                                continue
                            elif line.strip() and not flag:
                                new.write(line)
                    filecopy()
                    print("修改成功")
                else:
                    print("输入错误的序号")
            else:
                print("输入错误的序号")
        else:
            print("输入错误的序号")


# 删除HAproxy配置信息
def delinfo():
    """ 删除HAproxy配置信息 """
    print("删除backend和sever信息")
    domainList = getdominlist()
    for i in domainList:
        print(domainList.index(i), i)
    domain_num = input("请输入您要删除的域名序号：")
    if domain_num.isdigit():
        domain_int_num = int(domain_num)
        if domain_int_num < len(domainList):
            str_sip = """ 删除选项
             1.整个backend
             2.某条server信息"""
            print(str_sip)
            choose = input("您的选择：")
            if choose == '1':
                print("删除整个backend")
                with open(CFG_FILE, 'r') as old, open(CFG_FILE_TEMP, 'w', encoding='utf-8') as new:
                    flag = False
                    for line in old:
                        if line.strip().startswith("backend") and line.strip() == 'backend ' + domainList[domain_int_num]:
                            flag = True
                        elif flag and line.strip().startswith("backend"):
                            flag = False
                            new.write(line)
                        elif line.strip() and not flag:
                            new.write(line)
                filecopy()
                print("删除成功")
            elif choose == '2':
                print("删除某条server")
                server = getserver(domainList[domain_int_num])
                for i in server:
                    print(server.index(i), i)
                server_num = input("选择您要修改的server信息的序号:")
                if server_num.isdigit():
                    server_int_num = int(server_num)
                    if server_int_num < len(server):
                        with open(CFG_FILE, 'r') as old, open(CFG_FILE_TEMP, 'w', encoding='utf-8') as new:
                            flag = False
                            for line in old:
                                if line.strip().startswith("backend") and line.strip() == 'backend ' + domainList[domain_int_num]:
                                    flag = True
                                    new.write(line)
                                    for serverlist in server:
                                        if serverlist != server[server_int_num]:
                                            new.write(serverlist)
                                elif flag and line.strip().startswith("backend"):
                                    flag = False
                                    new.write(line)
                                elif line.strip() and not flag:
                                    new.write(line)
                        filecopy()
                    else:
                        print("输入错误的序号")
            else:
                print("输入错误的序号")
        else:
            print("输入错误的序号")


# 备份HAproxy配置文件
def bakupinfo():
    """ 备份HAproxy配置文件 """
    print("备份配置文件")
    shutil.copy(CFG_FILE, CFG_FILE_BAK)
    print("备份成功")


# 回滚HAproxy配置文件
def rollback():
    """ 回滚HAproxy配置文件 """
    print(" 回滚HAproxy配置文件 ")
    shutil.copy(CFG_FILE_BAK, CFG_FILE)
    print("回滚成功")


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

