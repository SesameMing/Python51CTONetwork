#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-28 22:00
import os
import pickle
import time
from modules import log
from modules.lib import teacher, course, student
from conf import setting

USER_LOGIN_STATUS = {'login': False, 'name': None}
USER_LOGIN_FILE = ''
QUIT_CHAR = 'q'


def xuanke():
    """ 学生选课 """
    filename = os.listdir(os.path.join(setting.COURSE_DIR_FILE))
    for cname in filename:
        print(cname)




def main():
    flag = True
    while flag:
        print_str = """------选课系统菜单---------
    欢迎学生：%s

    1.选课
    2.上课
    3.选课列表
    4.上课记录
    5.老师测评

    【数字】：选择  【%s】：退出
    ---------------------------------------""" % (USER_LOGIN_STATUS['name'], QUIT_CHAR)
        print(print_str)
        chooes = input(">>>:")
        if chooes == QUIT_CHAR:
            flag = False
            syslog1.info('%s 用户退出登录' % USER_LOGIN_STATUS['name'])
            continue
        else:
            if chooes.isdigit():
                chooes_int = int(chooes)
                if chooes_int == 1:
                    xuanke()
                elif chooes_int == 2:
                    pass
                elif chooes_int == 3:
                    pass
                elif chooes_int == 4:
                    pass
                elif chooes_int == 5:
                    pass

            else:
                syslog1.debug("输入错误")



def login():
    username = input("请输入登录姓名：").strip()
    password = input("请输入登录密码：").strip()
    if os.path.exists(os.path.join(setting.STUDEN_DIR_FILE, username)):
        user_db = pickle.load(open(os.path.join(setting.STUDEN_DIR_FILE, username, 'info.db'), 'rb'))
        if user_db.name == username and user_db.password == password:
            USER_LOGIN_STATUS['login'] = True
            USER_LOGIN_STATUS['name'] = username
            global syslog1
            USER_LOGIN_FILE = os.path.join(setting.STUDEN_DIR_FILE, username, 'user.log')
            logobj.setLoginpath(USER_LOGIN_FILE)

            global syslog1
            syslog1 = logobj.log2()
            syslog1.info('%s 用户登录成功 - 学生端' % username)
            time.sleep(.5)
            return True
    else:
        syslog.debug('帐号或密码错误')
        time.sleep(.5)
        return False


def run():
    global syslog
    global logobj
    logobj = log.loger()
    syslog = logobj.log()
    syslog.info('学生选课系统程序-学生端运行')
    time.sleep(.5)

    if login():
        main()
