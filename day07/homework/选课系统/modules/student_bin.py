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

def pingjia():
    print('-------评价老师列表-------')
    t_list = os.listdir(os.path.join(setting.TEACHER_DIR_FILE))
    for index, tname in enumerate(t_list):
        print(index, tname)
    choose = input(">>>请输入要评价老师的序号:")
    if choose.isdigit():
        if int(choose) <= len(t_list):
            t_db = pickle.load(open(os.path.join(setting.TEACHER_DIR_FILE, t_list[int(choose)], 'info.db'), 'rb'))
            str = "您选择了 %s 老师,请为他评价,好评或者差评<输入'好' 或者 '差'>：" % t_list[int(choose)]
            userinp = input(str).strip()
            if userinp == '好':
                t_db.addmoney(100)
                pickle.dump(t_db, open(os.path.join(setting.TEACHER_DIR_FILE, t_list[int(choose)], 'info.db'), 'wb'))
                syslog1.info('%s 用户评价 %s 成功 - 学生端' % (USER_LOGIN_STATUS['name'],
                                                      t_list[int(choose)]))
                time.sleep(.5)
                return True
            elif userinp == '差':
                t_db.addmoney(-100)
                pickle.dump(t_db, open(os.path.join(setting.TEACHER_DIR_FILE, t_list[int(choose)], 'info.db'), 'wb'))
                syslog1.info('%s 用户评价 %s 成功 - 学生端' % (USER_LOGIN_STATUS['name'],
                                                      t_list[int(choose)]))
                time.sleep(.5)
                return True
            else:
                syslog1.debug('输入选项不在范围之类 - 学生端')
                time.sleep(.5)
                return False
        else:
            syslog1.debug('输入选项不在范围之类 - 学生端')
            time.sleep(.5)
            return False
    else:
        syslog1.debug('输入选项不在范围之类 - 学生端')
        time.sleep(.5)
        return False



def shangkejilu():
    """ 上课记录 """
    user_db = pickle.load(open(os.path.join(setting.STUDEN_DIR_FILE, USER_LOGIN_STATUS['name'],
                                            'info.db'), 'rb'))
    print('----------请选择要查询课程的记录--------')
    for index, line in enumerate(user_db.shangkelist):
        print(index, line)
    print('--------------------------------------')
    choose = input(">>>请输入您的选择<课程名称>:").strip()
    if not choose.isdigit():
        for line in user_db.shangkelist[choose]:
            print(line)
        else:
            syslog1.debug('输入选项不在范围之类 - 学生端')
            time.sleep(.5)
            return False
    else:
        syslog1.debug('输入选项不在范围之类 - 学生端')
        time.sleep(.5)
        return False


def xuanke():
    """ 学生选课 """
    filename = os.listdir(os.path.join(setting.COURSE_DIR_FILE))
    print("--------选课系统--------")
    for index, cname in enumerate(filename):
        course_pic = pickle.load(open(os.path.join(setting.COURSE_DIR_FILE, cname, 'info.db'), 'rb'))
        print(index, cname, course_pic.teacher.name, course_pic.shangkeneirong)
    print("输入序号来选择课程")
    choose = input(">>>:")
    if choose.isdigit():
        if int(choose) <= len(filename):
            course_pic = pickle.load(open(os.path.join(setting.COURSE_DIR_FILE, filename[int(choose)],
                                                       'info.db'), 'rb'))
            user_db = pickle.load(open(os.path.join(setting.STUDEN_DIR_FILE, USER_LOGIN_STATUS['name'],
                                                    'info.db'), 'rb'))
            if course_pic.name not in user_db.getxunkelist():
                if user_db.addxuankelist(course_pic):
                    pickle.dump(user_db, open(os.path.join(setting.STUDEN_DIR_FILE, USER_LOGIN_STATUS['name'],
                                                           'info.db'), 'wb'))
                    syslog1.info('%s 用户选课 %s 成功 - 学生端' % (USER_LOGIN_STATUS['name'],
                                                          filename[int(choose)]))
                    time.sleep(.5)
                    return True
            else:
                syslog1.debug('该课程已经选过,请尝试选择其他课程 - 学生端')
                time.sleep(.5)
                return False
        else:
            syslog1.debug('输入选项不在范围之类 - 学生端')
            time.sleep(.5)
            return False


def shangke():
    """ 学生上课 """
    user_db = pickle.load(open(os.path.join(setting.STUDEN_DIR_FILE, USER_LOGIN_STATUS['name'],
                                            'info.db'), 'rb'))
    print('已经选择了的课程有：')
    for index, item in enumerate(user_db.getxunkelist()):
        print(index, item)
    uchoose = input(">>>选择宁要上的课程的序号:")
    if uchoose.isdigit():
        if int(uchoose) <= len(user_db.getxunkelist()):
            kechengname = user_db.getxunkelist()[int(uchoose)]
            for item in user_db.xuankelist:
                if kechengname == item.name:
                    user_db.addshangkelist(item)
                    pickle.dump(user_db,
                                open(os.path.join(setting.STUDEN_DIR_FILE, USER_LOGIN_STATUS['name'], 'info.db'),
                                     'wb'))
                    teacher_db = pickle.load(open(os.path.join(setting.TEACHER_DIR_FILE, item.teacher.name, 'info.db'),
                                                  'rb'))
                    teacher_db.addmoney(item.money)
                    pickle.dump(teacher_db, open(os.path.join(setting.TEACHER_DIR_FILE, item.teacher.name, 'info.db'),
                                     'wb'))
                    syslog1.info('%s 用户 %s 上课 - 学生端' % (USER_LOGIN_STATUS['name'], kechengname))
                    time.sleep(.5)
                    return True
        else:
            syslog1.debug('输入选项不在范围之类 - 学生端')
            time.sleep(.5)
            return False
    else:
        syslog1.debug('输入选项不在范围之类 - 学生端')
        time.sleep(.5)
        return False


def xuankeinfo():
    """ 学生选课信息 """
    user_db = pickle.load(open(os.path.join(setting.STUDEN_DIR_FILE, USER_LOGIN_STATUS['name'],
                                            'info.db'), 'rb'))
    print('已经选择了的课程有：')
    for index, item in enumerate(user_db.getxunkelist()):
        print(index, item)
    input(">>>任意键返回主菜单:")


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
------------------------------""" % (USER_LOGIN_STATUS['name'], QUIT_CHAR)
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
                    shangke()
                elif chooes_int == 3:
                    xuankeinfo()
                elif chooes_int == 4:
                    shangkejilu()
                elif chooes_int == 5:
                    pingjia()

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
