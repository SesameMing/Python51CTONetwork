#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-21 12:36
import os
import time
import json
import logging
from conf import setting
from bin.lib import host

USER_LOGIN_STATUS = {'login': False, 'username': None}
QUIT_CHAR = 'q'


def setloggin():
    logger = logging.getLogger("客户端程序")
    if not logging._handlers:
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s %(levelname)s] %(message)s'))
        logger.addHandler(ch)
    return logger


Log = setloggin()




def login():
    Log.info("用户登录")
    time.sleep(.1)
    while True:
        username = input("请输入账号：").strip()
        password = input("请输入密码：").strip()
        if os.path.exists(os.path.join(setting.USER_DIR_PATH, username)):
            if os.path.exists(os.path.join(setting.USER_DIR_PATH, username, 'user.config')):
                user_dic = json.load(open(os.path.join(setting.USER_DIR_PATH, username, 'user.config'), 'r'))
                if username == user_dic.get('username') and password == user_dic.get('password'):
                    USER_LOGIN_STATUS['login'] = True
                    USER_LOGIN_STATUS['username'] = username
                    Log.info('登录成功')
                    return True
        Log.warning("帐号或密码错误")
        time.sleep(.1)


# 检查用户登录状态
def check_login(func):
    if USER_LOGIN_STATUS['login'] is False or USER_LOGIN_STATUS['username'] is None:
        Log.warning("请先登录")
        login()
    else:
        return func()


# 添加主机分组
def addhostclass():
    while True:
        innp = input("请输入主机分组名称>>>:").strip()
        if os.path.exists(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config')):
            host_dic = json.load(open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config'), 'r'))
            if host_dic.get(innp) is None:
                host_dic[innp] = []
            else:
                Log.warning("该分组已经存在,请重新输入")
                continue
        else:
            host_dic = {innp: []}
        json.dump(host_dic,
                  open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config'), 'w'))
        Log.warning("添加成功")
        break


# 添加主机
def addhost():
    if os.path.exists(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config')):
        host_dic = json.load(
            open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config'), 'r'))
        if len(host_dic) > 0:
            innp_name = input("准备输入主机名称(备注)>>>：")
            innp_ip = input("准备输入主机ip>>>：")
            innp_port = input("准备输入主机端口)>>>：")
            Log.info("正在验证主机是否存在，请稍等..")
            if host.yzhost(innp_ip, innp_port):
                while True:
                    Log.info("验证权限")
                    innp_username = input("请输入主机帐号：")
                    innp_password = input("请输入主机密码：")
                    Log.info("正在验证主机权限，请等待...")
                    if host.yzauth(innp_ip, innp_port, innp_username, innp_password):
                        pass
                    else:
                        Log.warning("帐号密码验证错误")
                        time.sleep(.1)
                        continue

    Log.warning("还没设置主机分组，请先添加主机分组")
    time.sleep(.1)
    addhostclass()


# 显示主机列表
def showhost():
    if os.path.exists(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config')):
        print("--------主机列表---------")
        host_dic = json.load(
            open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config'), 'r'))
        for hostclass in host_dic:
            print("分组 ：%s" % hostclass)
            if len(host_dic.get(hostclass)) == 0:
                print(" └    暂无主机")
            else:
                for hostlist in host_dic.get(hostclass):
                    print(" └  主机 ：%s" % hostlist)

        print("------------------------")
        print("1.添加主机  其他：返回主菜单")
        innp = input(">>>:").strip()
        if innp == '1':
            addhost()
    else:
        print_s = """
还没有主机记录，请添加主机

1. 添加主机
2. 返回
        """
        print(print_s)
        innp = input(">>>:")
        if innp == '1':
            addhost()
        else:
            pass


# 主机管理
def adminhost():
    pass


def main():
    while True:
        str1 = """
主机管理系统 v1.0
-----------------------------------
1. 查看主机
2. 查看主机分组
3. 下发任务
4. 连接主机
5. 修改帐号密码

----------------------------------
数字：选择        %s：退出
----------------------------------
""" % QUIT_CHAR
        print(str1)
        inpp = input(">>>:")
        if inpp == '1':
            showhost()
        elif inpp == '2':
            pass
        elif inpp == '3':
            pass
        elif inpp == 'q':
            Log.info("退出程序")
            break
        else:
            pass


def check_conf_file():
    Log.info("检查配置文件")
    if os.path.exists(os.path.join(setting.USER_DIR_PATH)):
        if len(os.listdir(os.path.join(setting.USER_DIR_PATH))) > 0:
            return True
    else:
        os.makedirs(os.path.join(setting.USER_DIR_PATH))
    Log.info("程序第一次运行，请先设置登录用户信息")
    time.sleep(.1)
    username = input("设置登录的帐号：")
    password = input("设置登录的密码：")
    dic = {'username': username, 'password': password}
    os.makedirs(os.path.join(setting.USER_DIR_PATH, username))
    json.dump(dic, open(os.path.join(setting.USER_DIR_PATH, username, 'user.config'), 'w'))
    Log.info("初次启动文件配置成功")


def run():
    Log.info("启动")
    check_conf_file()
    if login():
        time.sleep(.1)
        main()


if __name__ == '__main__':
    main()
