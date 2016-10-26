#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-21 12:36
import os
import time
import json
import logging
import threading
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


def xgpassword():
    if os.path.exists(os.path.join(setting.USER_DIR_PATH,  USER_LOGIN_STATUS['username'], 'user.config')):
        user_dic = json.load(open(os.path.join(setting.USER_DIR_PATH,  USER_LOGIN_STATUS['username'], 'user.config'),
                                  'r'))
        old_password = input("请输入原始密码：")
        new_password = input("请输入新密码：")
        if user_dic['password'] == old_password:
            user_dic['password'] = new_password
            json.dump(user_dic, open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'user.config'),
                                     'w'))
            Log.info("密码修改成功")
            time.sleep(.1)
        else:
            Log.warning("密码修改失败，原密码不正确")
            time.sleep(.1)
    else:
        Log.warning("非法操作")  # 正常情况下不会出现这个选项
        time.sleep(.1)


# 下发任务
def xiafaru():
    if os.path.exists(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config')):
        host_dic = json.load(
            open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config'), 'r'))
        for hostclass in host_dic:
            print("分组 ：%s" % hostclass)
            if len(host_dic.get(hostclass)) == 0:
                print(" └  暂无主机")
            else:
                for hostlist in host_dic.get(hostclass):
                    print(" └ 主机: %s ip:%s " % (hostlist[0], hostlist[1]))
        print_str = """选择分组还是具体的服务器
1.服务器分组
2.单独服务器
"""
        print(print_str)
        uinnp = input(">>>:")
        if uinnp == '1':
            host_index = []
            for hostclass in host_dic:
                host_index.append(hostclass)
            for index, host_item in enumerate(host_index):
                print("%s,  %s" % (index, host_item))
            host_class_num = input(">>>:")
            host_list = host_dic.get(host_index[int(host_class_num)])
            if len(host_list) > 0:
                print("------主机列表-------")
                for item in host_list:
                    print("%s %s" % (item[0], item[1]))
                while True:
                    cmd = input("[%s:退出]选择进行的操作的命令>>>>:" % QUIT_CHAR).strip()
                    thread_list = []
                    # 命令不能为空
                    if cmd == QUIT_CHAR:
                        Log.info("退出，返回主菜单")
                        break
                    if cmd:
                        for item in host_list:
                            func = host.HostClent(item[1], item[2], item[3], item[4])
                            t = threading.Thread(target=func.run, args={cmd})
                            t.start()
                            thread_list.append(t)
                        for t in thread_list:
                            t.join()
            else:
                Log.warning("选择的分组下没有主机")
                time.sleep(.1)

        elif uinnp == '2':
            host_list = []
            for item in host_dic:
                for hostlist in host_dic[item]:
                    host_list.append(hostlist)
            for index, hosts in enumerate(host_list):
                print("%s. %s ip:%s " % (index, hosts[0], hosts[1]))
            innp = input("[%s:退出]选择要链接的服务器序号>>>：" % QUIT_CHAR).strip()
            if innp.isdigit():
                if int(innp) < len(host_list):
                    print("您选择了主机：%s  ip：%s " % (host_list[int(innp)][0], host_list[int(innp)][1]))
                    while True:
                        cmd = input("[%s:退出]选择进行的操作的命令>>>：" % QUIT_CHAR).strip()
                        # 命令不能为空
                        if cmd == QUIT_CHAR:
                            Log.info("退出，返回主菜单")
                            break
                        if cmd:
                            func = host.HostClent(host_list[int(innp)][1], host_list[int(innp)][2],
                                                  host_list[int(innp)][3], host_list[int(innp)][4],
                                                  )
                            func.run(cmd)
                else:
                    Log.warning("错误选择")
                    time.sleep(.1)
            else:
                Log.info("返回主菜单")
                time.sleep(.1)
        else:
            Log.warning("错误的选择，返回主菜单")
            time.sleep(.1)


# 链接服务器
def lianjiefuwuqi():
    if os.path.exists(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config')):
        host_dic = json.load(open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'],
                                               'host.config'), 'r'))
        host_list = []
        for item in host_dic:
            for hostlist in host_dic[item]:
                host_list.append(hostlist)
        for index, hosts in enumerate(host_list):
            print("%s. %s ip:%s " % (index, hosts[0], hosts[1]))
        if len(host_list) > 0:
            innp = input("<%s:退出>选择要链接的服务器序号>>>：" % QUIT_CHAR).strip()
            if innp.isdigit():
                if int(innp) < len(host_list):
                    host_action = host.HostClent(host_list[int(innp)][1], int(host_list[int(innp)][2]), host_list[int(innp)][3], host_list[int(innp)][4])
                    if host_action.ssh_host():
                        Log.info("链接成功")
                        time.sleep(.1)
                        while True:
                            # cd 方法转换成ls 方法
                            innp_commend = input("[<%s:退出>%s@%s]:" % (QUIT_CHAR, host_list[int(innp)][3], host_list[int(innp)][0]))
                            if innp_commend == QUIT_CHAR:
                                break
                            host_action.run(innp_commend)
                    else:
                        Log.warning("链接失败，请检查网络是否通畅或者服务器帐号密码是否正确")
                else:
                    Log.warning("输入的不在范围内")
            else:
                pass
        else:
            Log.warning("不存在主机,请先添加主机")
    else:
        Log.warning("不存在主机,请先添加主机")


# 显示分组
def showclass():
    flag = True
    while flag:
        if os.path.exists(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'], 'host.config')):
            host_dic = json.load(open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'],
                                                   'host.config'), 'r'))
            print("分组")
            classname = []
            for item in host_dic:
                classname.append(item)
            for index, hostclass in enumerate(classname):
                print("└ %s. %s ip:%s " % (index, hostclass[0], hostclass[1]))
            print_str = """---------------------------
数字：查看分类下的主机
add: 添加分类 del：删除分类 edt：修改分类名称
其他：退出
"""
            print(print_str)
            innp = input(">>>:").strip()
            if innp == 'add':
                addhostclass()
            elif innp == 'del':
                n_innp = input("输入要删除的分组id序号>>>:").strip()
                if int(n_innp) < len(classname):
                    t_inpp = input("确定要删除分类【%s】以及分类下的主机吗？<y/n>" % classname[int(n_innp)]).strip()
                    if t_inpp == 'y':
                        del host_dic[classname[int(n_innp)]]
                        json.dump(host_dic, open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'],
                                                              'host.config'), 'w'))
                        Log.info('删除分组成功')
                        time.sleep(.1)
                    print(classname[int(n_innp)])
                else:
                    print("输入的数字不在范围内")

            elif innp == 'edt':
                n_innp = input("输入要修改的分组id序号>>>:").strip()
                if int(n_innp) < len(classname):
                    t_inpp = input("修改分类【%s】的名称为：" % classname[int(n_innp)]).strip()
                    if t_inpp not in classname:
                        host_dic[t_inpp] = host_dic[classname[int(n_innp)]]
                        del host_dic[classname[int(n_innp)]]
                        json.dump(host_dic, open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'],
                                                              'host.config'), 'w'))
                        Log.info("新名称修改成功")
                    else:
                        Log.warning("新名称在分类中已经存在")
                else:
                    print("输入的数字不在范围内")

            else:
                flag = False
                continue

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
            while True:
                innp_name = input("准备输入主机名称(备注)：").strip()
                while bool(innp_name) is False:
                    innp_name = input("主机名称(备注)不能为空：").strip()
                innp_ip = input("准备输入主机ip：").strip()
                while bool(innp_ip) is False:
                    innp_ip = input("ip不能为空：").strip()
                innp_port = input("准备输入主机端口：").strip()
                while bool(innp_port) is False:
                    innp_port = 22
                    print("默认端口号为:22")
                innp_username = input("请输入主机帐号：").strip()
                while bool(innp_username) is False:
                    innp_username = input("主机帐号不能为空：").strip()
                innp_password = input("请输入主机密码：").strip()
                while bool(innp_password) is False:
                    innp_password = input("主机密码不能为空：").strip()
                Log.info("正在验证主机是否存在，请稍等..")
                host_action = host.HostClent(innp_ip, innp_port, innp_username, innp_password)
                if host_action.ssh_host():
                    Log.info("验证成功,请选择分类:")
                    print("验证成功,请选择分类:")
                    time.sleep(.1)
                    classname = []
                    for item in host_dic:
                        classname.append(item)
                    for index, items in enumerate(classname):
                        print("%s . %s" % (index, items))
                    classnum = input(">>>:")
                    if int(classnum) < len(classname):
                        host_dic[classname[int(classnum)]].append([innp_name, innp_ip, innp_port, innp_username, innp_password])
                        json.dump(host_dic,
                                  open(os.path.join(setting.USER_DIR_PATH, USER_LOGIN_STATUS['username'],
                                                    'host.config'), 'w'))
                        Log.info("添加成功")
                        time.sleep(.1)
                        break
                else:
                    Log.info("验证失败")
                    time.sleep(.1)
    else:
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
                print(" └  暂无主机")
            else:
                for hostlist in host_dic.get(hostclass):
                    print(" └ 主机: %s ip:%s " % (hostlist[0], hostlist[1]))
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
            showclass()
        elif inpp == '3':
            xiafaru()
        elif inpp == '4':
            lianjiefuwuqi()
        elif inpp == '5':
            xgpassword()
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
