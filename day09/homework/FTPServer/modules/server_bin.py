#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-05 23:48
import os
import time
import json
import socket
import socketserver
from modules.lib import log
from conf import setting
logmsg= log.log()
ip_port = ()
QUIT_CHAR = 'q'

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print(len(data))
        data = json.loads(data.decode())
        print(data)
        if not os.path.exists(os.path.join(setting.USER_CONFIG_DIR, data.get('username'))) or \
                not os.path.exists(os.path.join(setting.USER_HOME_DIR, data.get('username'))):
            self.request.sendall(bytes('文件目录不存在', encoding='utf-8'))
        logmsg.debug("%s 链接了服务端" % self.client_address[0])


def adduser():
    """ 添加FTP用户 """
    username = input("新用户名：").strip()
    while not username:
        username = input("用户名不能为空,请重新输入：").strip()
    password = input("新用户密码：").strip()
    while not password:
        password = input("密码不能为空,请重新输入：").strip()



def showuser():
    """ 显示用户列表  """
    print_str ="""
------------------------------------------------------------------------
|            　　　　        查看用户列表                　　　　      |
------------------------------------------------------------------------
| 用户名  |分配内存|可用内存|                home目录  　              |"""
    print(print_str)
    user_list = [
        ['damig', '50M', '49M', 'C://XASDASDASD/damig'],
        ['szy', '50M', '49M', 'C://XASDASDASD/szy']
                 ]
    for item in user_list:
        user_list_tp = "|{:^9}|{:^8}|{:^8}|{:^42}|".format(*item)
        print(user_list_tp)

def startServer():
    """ 启动FTPserver服务 """
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
    server.serve_forever()


def run():
    print_str = """
----------------------------------
|       FTP Server v 1.0         |
----------------------------------
|    1.启动FTPServer             |
|    2.查看用户                  |
|    2.添加用户                  |
|    3.修改用户                  |
|    4.删除用户以及用户目录      |
|                                |
----------------------------------
|     数字：选择     %s: 退出     |
----------------------------------""" % QUIT_CHAR
    print(print_str)
    choose = input(">>>:")
    if choose == '1':
        startServer()
    elif choose == '2':
        showuser()
    elif choose == 'q':
        logmsg.debug('FTPServer退出')


if __name__ == '__main__':
    run()