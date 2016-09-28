#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-27 15:07

# user_dic = {'username': username, 'password': password}
import os
import pickle
import time
from modules import log
from modules.lib import teacher, course
from conf import setting

USER_LOGIN_STATUS = {'login': False, 'name': None}
USER_LOGIN_FILE = ''
QUIT_CHAR = 'q'


def createcourse():
    """ 创建课程 """
    kname = input("<提示:课程名称不能纯数字>看新课程名称：").strip()
    if kname.isdigit():
        syslog1.debug('课程名称不能为纯数字, 返回主菜单')
        time.sleep(.5)
        return False
    kmoney = input("<提示:0-99999>课程课时费：").strip()
    if not kmoney.isdigit():
        syslog1.debug('课时费只能为数字, 返回主菜单')
        time.sleep(.5)
        return False
    kneirong = input("请输入上课内容：").strip()
    if not kneirong:
        syslog1.debug('上课内容不能为空')
        time.sleep(.5)
        return False
    filename = os.listdir(os.path.join(setting.TEACHER_DIR_FILE))
    print("---------老师列表-----------")
    for name in filename:
        print(name)
    print("---------------------------")
    teachername = input("<提示：输入老师姓名>请输入要查看的老师姓名：").strip()
    if not os.path.exists(os.path.join(setting.TEACHER_DIR_FILE, teachername)):
        syslog1.debug('上课老师不存在')
        time.sleep(.5)
        return False
    else:
        teacher_info = pickle.load(open(os.path.join(setting.TEACHER_DIR_FILE, teachername, 'info.db'), 'rb'))
    new_course = course.course(kname, kmoney, teacher_info, kneirong)
    if not os.path.exists(os.path.join(setting.COURSE_DIR_FILE, kname)):
        os.makedirs(os.path.join(setting.COURSE_DIR_FILE, kname))
    pickle.dump(new_course, open(os.path.join(setting.COURSE_DIR_FILE, kname, 'info.db'), 'wb'))
    syslog1.info('%s 创建了新的课程 %s' % (USER_LOGIN_STATUS['name'], kname))
    time.sleep(.5)
    print(new_course.getteacher())
    return True


def showteteacher():
    """ 查看课程信息 """
    filename = os.listdir(os.path.join(setting.TEACHER_DIR_FILE))
    print("---------老师列表-----------")
    for name in filename:
        print(name)
    print("请输入要查看的老师姓名")
    print("---------------------------")
    name = input(">>>:").strip()
    if not os.path.exists(os.path.join(setting.TEACHER_DIR_FILE, name)):
        syslog1.debug('查询的老师不存在，退出')
        time.sleep(.5)
        return False
    else:
        teacher_obj = pickle.load(open(os.path.join(setting.TEACHER_DIR_FILE, name, 'info.db'), 'rb'))
        teacher_info = teacher_obj.userinfo()
        print_tpl = """--------老师信息----------
老师姓名：{}
老师年龄：{}
老师性别：{}
老师资产：{}
---------------------------""".format(teacher_info['name'], teacher_info['age'], teacher_info['gender'],
                                      teacher_info['money'])
        print(print_tpl)
        syslog1.debug('成功查询了 %s 老师信息' % name)
        time.sleep(.5)
        return True


def createteacher():
    """ 添加老师信息 """
    name = input("<提示：不能是纯数字>老师姓名：").strip()
    if name.isdigit():
        syslog1.debug('老师姓名不能为纯数字，退出')
        time.sleep(.5)
        return False
    age = input("<提示：0-99>老师年龄：").strip()
    if not age.isdigit():
        syslog1.debug('年龄不能为非数字，退出')
        time.sleep(.5)
        return False
    gender = input("<提示：男or女>性别：").strip()
    if gender not in ['男', '女']:
        syslog1.debug('性别只能为"男"or"女"')
        time.sleep(.5)
        return False

    new_teacher = teacher.teacher(name, age, gender)
    if not os.path.exists(os.path.join(setting.TEACHER_DIR_FILE, name)):
        os.makedirs(os.path.join(setting.TEACHER_DIR_FILE, name))
        pickle.dump(new_teacher, open(os.path.join(setting.TEACHER_DIR_FILE, name, 'info.db'), 'wb'))
        syslog1.info('创建了新老师 %s 信息' % name)
        time.sleep(.5)
        return True
    else:
        syslog1.debug('老师已经存在')
        time.sleep(.5)
        return False


def main():
    flag = True
    while flag:
        print_str = """ ------------管理员菜单---------------
1. 添加老师信息
2. 查看老师信息
3. 添加课程信息
4. 查看课程信息
5. 添加学生信息
6. 查看学生信息

【数字】：选择  【%s】：退出
---------------------------------------""" % QUIT_CHAR
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
                    createteacher()
                elif chooes_int == 2:
                    showteteacher()
                elif chooes_int == 3:
                    createcourse()

            else:
                syslog1.debug("输入错误")


def login():
    username = input("请输入帐号：")
    password = input("请输入密码：")
    if os.path.exists(os.path.join(setting.ADMIN_DIR_FILE, username)):
        use_dic = pickle.load(open(os.path.join(setting.ADMIN_DIR_FILE, username, 'info.db'), 'rb'))
        if use_dic['username'] == username and use_dic['password'] == password:
            USER_LOGIN_STATUS['login'] = True
            USER_LOGIN_STATUS['name'] = username
            USER_LOGIN_FILE = os.path.join(setting.ADMIN_DIR_FILE, username, 'user.log')
            logobj.setLoginpath(USER_LOGIN_FILE)

            global syslog1
            syslog1 = logobj.log2()
            syslog1.info('%s 用户登录成功' % username)
            time.sleep(.5)
            return True

        else:
            syslog.debug("用户登录 密码错误")
    else:
        syslog.debug("用户登录 密码错误")


def run():
    global syslog
    global logobj
    logobj = log.loger()
    syslog = logobj.log()
    syslog.info('执行程序')
    time.sleep(.5)

    if login():
        main()


if __name__ == '__main__':
    main()
