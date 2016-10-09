#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-05 23:48
import os
import sys
import time
import json
import socket
import shutil
import hashlib
import subprocess
import socketserver
from modules.lib import log, ftpserver
from conf import setting
logmsg= log.log()
ip_port = ()
QUIT_CHAR = 'q'


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        data = json.loads(data.decode())
        if not os.path.exists(os.path.join(setting.USER_CONFIG_DIR, data.get('username'))) or \
                not os.path.exists(os.path.join(setting.USER_HOME_DIR, data.get('username'))):
            self.request.sendall(bytes('用户名或密码不正确', encoding='utf-8'))
            logmsg.debug("%s 尝试用 %s 链接,但是，用户或HOME目录不存在" % (self.client_address[0], data.get('username')))
        else:
            user_dic = json.load(open(os.path.join(setting.USER_CONFIG_DIR, data.get('username'), 'user.config'), 'r'))
            if user_dic.get('username') == data.get('username') and data.get('password') == user_dic.get('password'):
                logmsg.debug("%s 用 %s 链接了服务端" % (self.client_address[0], data.get('username')))
                self.request.sendall(bytes('欢迎 %s 登录到FTP服务器' % data.get('username'), encoding='utf-8'))
                data = self.request.recv(1024)
                # 返回用户家目录
                data = "dir %s" % (os.path.join(setting.USER_HOME_DIR, user_dic.get('username'),))
                p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
                send_data = p.stdout.read()
                send_data = str(send_data, encoding='gbk')
                self.request.sendall(bytes(send_data, encoding='utf8'))

                # 开始循环接收
                while True:
                    try:
                        recv_data = self.request.recv(1024)
                        if len(recv_data) == 0:
                            break
                        print(recv_data.decode())
                        recv_data = recv_data.decode().split(' ')
                        print(recv_data)
                        obj = ftpserver.ftpserver()
                        if hasattr(obj, recv_data[0]):
                            fun = getattr(obj, recv_data[0])
                            fun(self)
                        # self.request.sendall(bytes("卡住", encoding='utf8'))
                    except Exception as e:
                        print(e)
                        logmsg.debug("%s 断开了服务端" % (self.client_address[0]))
                        break

            else:
                logmsg.debug("%s 尝试用 %s 链接,但是密码错误" % (self.client_address[0], data.get('username')))
                self.request.sendall(bytes('用户名或密码不正确', encoding='utf-8'))
                sys.exit()


def FileSize(path):
    """

    计算目录下的所有文件的大小

    """
    size = 0
    for root, dirs, files in os.walk(path, True):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        # 目录下文件大小累加
    return size


def deluser():
    """

    删除用户以及home目录

    """
    userlist = os.listdir(os.path.join(setting.USER_CONFIG_DIR))
    for index, name in enumerate(userlist):
        print(index, name)
    chooes = input("请选择要删除的用户序号>>>:")
    if chooes.isdigit():
        if int(chooes) <= len(userlist):
            zfqr = input("是否确认立即删除用户以及其目录[y/n]:")
            if zfqr == 'y' or zfqr == 'Y':
                if os.path.exists(os.path.join(setting.USER_CONFIG_DIR, userlist[int(chooes)])):
                    shutil.rmtree(os.path.join(setting.USER_CONFIG_DIR, userlist[int(chooes)]))
                if os.path.exists(os.path.join(setting.USER_HOME_DIR, userlist[int(chooes)])):
                    shutil.rmtree(os.path.join(setting.USER_HOME_DIR, userlist[int(chooes)]))
                logmsg.debug("成功删除了 %s 用户以及其目录" % userlist[int(chooes)])
    else:
        logmsg.debug("输入不正确。")


def edituser():
    userlist = os.listdir(os.path.join(setting.USER_CONFIG_DIR))
    for index, name in enumerate(userlist):
        print(index, name)
    chooes = input("请选择要修改的用户序号>>>:")
    if chooes.isdigit():
        if int(chooes) <= len(userlist):
            user_dic = json.load(open(os.path.join(setting.USER_CONFIG_DIR, userlist[int(chooes)], 'user.config'), 'r'))
            str1 = """
用户名：{username}
分配存储：{storesizi}MB

1.修改密码
2.修改存储大小
""".format(**user_dic)
            print(str1)
            choose_set = input("输入您的选择>>>:")
            if choose_set == '1':
                new_password = input("请输入新密码：").strip()
                if not new_password:
                    new_password = input("密码不能为空，请重新输入：").strip()
                obj = hashlib.md5()
                obj.update(bytes(new_password, encoding='utf-8'))
                new_password = obj.hexdigest()
                user_dic['password'] = new_password
                json.dump(user_dic, open(os.path.join(setting.USER_CONFIG_DIR, userlist[int(chooes)], 'user.config'),
                                         'w'))
                logmsg.debug("成功修改了 %s 的密码" % userlist[int(chooes)])
                return True
            elif choose_set == '2':
                storesizi = input("请输入新的配额：").strip()
                if not storesizi:
                    storesizi = input("新的配额不能为空，请重新输入：").strip()
                user_dic['storesizi'] = storesizi
                json.dump(user_dic, open(os.path.join(setting.USER_CONFIG_DIR, userlist[int(chooes)], 'user.config'),
                                         'w'))
                logmsg.debug("成功修改了 %s 的配额" % userlist[int(chooes)])
                return True
            else:
                pass
    else:
        logmsg.debug("输入不符合规范")


def adduser():
    """

    添加FTP用户

    """
    username = input("新用户名：").strip()
    while not username:
        username = input("用户名不能为空,请重新输入：").strip()
    password = input("新用户密码：").strip()
    while not password:
        password = input("密码不能为空,请重新输入：").strip()
    obj = hashlib.md5()
    obj.update(bytes(password, encoding='utf-8'))
    password = obj.hexdigest()

    storesizi = input("分配存储空间大小(MB):").strip()
    while not storesizi:
        storesizi = input("分配存储空间大小不能为空,请重新输入：").strip()
    userdic = {'username': username, 'password': password, 'storesizi': storesizi, 'usesizi': 0}
    if not os.path.exists(os.path.join(setting.USER_CONFIG_DIR, username)):
        os.makedirs(os.path.join(setting.USER_CONFIG_DIR, username))
        json.dump(userdic, open(os.path.join(setting.USER_CONFIG_DIR, username, 'user.config'), 'w'))
        if not os.path.exists(os.path.join(setting.USER_HOME_DIR, username)):
            os.makedirs(os.path.join(setting.USER_HOME_DIR, username))
        logmsg.debug("创建FTP用户： %s 成功" % username)
        return True
    else:
        logmsg.debug("%s 用户已经存在" % username)
        return False


def showuser():
    """

    显示用户列表

    """
    info_sum_list = []
    user_dir_name = os.listdir(os.path.join(setting.USER_CONFIG_DIR))
    for iteminfo in user_dir_name:
        info_list = []
        info = json.load(open(os.path.join(setting.USER_CONFIG_DIR, iteminfo, 'user.config')))
        info_list.append(info.get('username'))
        info_list.append(info.get('storesizi'))
        size = FileSize(os.path.join(setting.USER_HOME_DIR, iteminfo)) / 1024 / 1024
        info_list.append("%.2f" % size)
        info_list.append(os.path.join(setting.USER_HOME_DIR, info.get('username')))
        info_sum_list.append(info_list)

    print_str = """【查看用户列表】                　　　　

| 用户名  |分配内存|可用内存|home目录  　               """
    print(print_str)
    for item in info_sum_list:
        user_list_tp = "|{:^9}|{:^6}MB|{:^6}MB|{:^42}".format(*item)
        print(user_list_tp)
    input("任意输入返回主菜单>>>:")


def editport():
    """

    修改FTP端口

    """
    if os.path.exists(os.path.join(setting.SERVER_CONFIG_DIR, 'server.db')):
        conf_dic = json.load(open(os.path.join(setting.SERVER_CONFIG_DIR, 'server.db'), 'r'))
        print("默认上次设置端口号：%s" % conf_dic.get('port'))
        new_port = input("请输入新的端口号：")
        conf_dic['port'] = new_port
    else:
        print("FTP还未设置端口号")
        new_port = input("请设置端口号：")
        conf_dic = {"port": str(new_port)}

    json.dump(conf_dic, open(os.path.join(setting.SERVER_CONFIG_DIR, 'server.db'), 'w'))
    logmsg.debug("FTP端口号更新为 %s" % new_port)
    cq = input("是否立即启动FTP服务[y/n]:")
    if cq == 'y' or cq == 'Y':
        startServer()
    else:
        logmsg.debug("即将主菜单")
        time.sleep(.5)


def startServer():
    """

    启动FTPserver服务

    """
    logmsg.debug("服务端开启")
    time.sleep(.5)
    logmsg.debug("正在初始化服务端软件")
    server_name = socket.gethostname()
    ip = socket.gethostbyname(server_name)
    logmsg.debug("服务端ip：%s" % ip)
    if not os.path.exists(os.path.join(setting.SERVER_CONFIG_DIR, 'server.db')):
        if not os.path.exists(setting.SERVER_CONFIG_DIR):
            os.makedirs(setting.SERVER_CONFIG_DIR)
        logmsg.debug("第一次登录，需要配置端口信息")
        time.sleep(.5)
        port = input("设置服务端口号<推荐1024-9999>：")
        server_conf = {"port": str(port)}
        json.dump(server_conf, open(os.path.join(setting.SERVER_CONFIG_DIR, 'server.db'), 'w'))
    else:
        server_conf = json.load(open(os.path.join(setting.SERVER_CONFIG_DIR, 'server.db'), 'r'))
    logmsg.debug("服务端端口号：%s" % int(server_conf.get('port')))
    ip_port = (ip, int(server_conf.get('port')))
    logmsg.debug("正在启动服务")
    server = socketserver.ThreadingTCPServer(ip_port, MyServer)
    logmsg.debug("启动服务成功，等待用户接入")
    server.serve_forever()


def run():
    print(sys.stdin.encoding)
    while True:
        print_str = """
----------------------------------
|       FTP Server v 1.0         |
----------------------------------
|    1.启动FTPServer             |
|    2.修改FTPServer端口         |
|    3.查看用户                  |
|    4.添加用户                  |
|    5.修改用户                  |
|    6.删除用户以及用户目录      |
|                                |
----------------------------------
|     数字：选择     %s: 退出     |
----------------------------------""" % QUIT_CHAR

        print(print_str)
        choose = input(">>>:")
        if choose == '1':
            startServer()
        elif choose == '2':
            editport()
        elif choose == '3':
            showuser()
        elif choose == '4':
            adduser()
        elif choose == '5':
            edituser()
        elif choose == '6':
            deluser()
        elif choose == 'q':
            logmsg.debug('FTPServer退出')


if __name__ == '__main__':
    run()