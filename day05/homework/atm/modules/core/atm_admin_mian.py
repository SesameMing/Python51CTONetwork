#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-15 19:50
# atm程序主程序


import os
import json
import time
import shutil
import logging
from conf import setting
QUIT_CHAR = 'q'  # 退出程序字符
USER_STATUS = {'IS_LOGIN': False, 'LOGIN_USER_NAME': None}  # 用户登录状态
logging.basicConfig(filename=os.path.join(setting.ADMIN_DIR_FOLDER, 'admin.log'), level=logging.INFO, format='%(asctime)s %(message)s',  datefmt='%m/%d/%Y %I:%M:%S %p')

def delUser():
    """
    删除用户
    """
    cardnum = input("请输入要设置的卡号：")
    if cardnum.isdigit():
        if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, cardnum)):
            restult = input("<y：确定>确定将该卡用户删除：")
            if restult == 'y':
                shutil.rmtree(os.path.join(setting.USER_DIR_FOLDER, cardnum))
                print("删除用户成功")
                logging.info('%s 删除了卡号：%s ' % (USER_STATUS['LOGIN_USER_NAME'], cardnum))
            else:
                print("取消删除")
        else:
            print("您输入的卡号不存在")
    else:
        print("您输入的卡号不符合规范")


def stopUser():
    """
    冻结用户
    """
    cardnum = input("请输入要设置的卡号：")
    if cardnum.isdigit():
        if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, cardnum)):
            restult = input("<y：确定>确定将该卡设置为禁用：")
            if restult == 'y':
                info_dic = json.load(open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json'), 'r'))
                info_dic['status'] = 0
                json.dump(info_dic, open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json'), 'w'))
                print("该用户已被禁用")
                logging.info('%s 冻结了卡号：%s ' % (USER_STATUS['LOGIN_USER_NAME'], cardnum))
            else:
                print("取消设置")

        else:
            print("您输入的卡号不存在")
    else:
        print("您输入的卡号不符合规范")

def setUserED():
    """
    设置用户额度
    """
    cardnum = input("请输入要设置的卡号：")
    if cardnum.isdigit():
        if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, cardnum)):
            info_dic = json.load(open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json'), 'r'))
            print("该用户现有额度： %s" % (info_dic['cradit']))
            ed = input("请输入新的用户额度：")
            if ed.isdigit():
                ed_int = int(ed)
                set_ed = json.load(open(setting.SET_DIR_FILE, "r"))
                if ed_int <= set_ed['max_ed']:
                    info_dic['cradit'] = ed
                    json.dump(info_dic, open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json'), 'w'))
                    print("修改成功")
                    logging.info('$s 修改了卡号：%s 的信用额度为 %s' % (USER_STATUS['LOGIN_USER_NAME'], cardnum, ed))
                else:
                    print("设置的额度超过设置的最大信用额度")
            else:
                print("输入的额度不符合规范")

        else:
            print("您输入的卡号不存在")
    else:
        print("您输入的卡号不符合规范")


def addUser():
    """
    添加用户
    """
    cardnum = input("请输入创建的卡号：")
    if cardnum.isdigit():
        if not os.path.exists(os.path.join(setting.USER_DIR_FOLDER, cardnum)):
            username = input("设置姓名：")
            if username.isdigit():
                print("姓名不能为纯数字")
                return False

            password = input("设置密码：")

            credit = input("信用卡额度：")
            if not credit.isdigit():
                print("输入的信用卡额度不符合规范")
                return False

            set_dict = json.load(open(setting.SET_DIR_FILE, 'r'))
            if int(credit) <= int(set_dict['max_ed']):
                cardinfo = {
                    "cardnum": cardnum,
                    "username": username,
                    "password": password,
                    "cradit": credit,
                    "kycradit": credit,
                    "balance": 0,
                    "enroll_date": time.time(),
                    "expire_date": time.time()+157680000,
                    "status": 1,
                    "debt": [],

                }
                os.makedirs(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'cardinfo'))
                json.dump(cardinfo, open(os.path.join(setting.USER_DIR_FOLDER, cardnum, "basic_info.json"), 'w'))
                logging.info('%s 添加新卡号：%s ' % (USER_STATUS['LOGIN_USER_NAME'], cardnum))
                print("新用户添加成功")
            else:
                print("超过了设置的最大信用额度")
        else:
            print("卡号存在")
    else:
        print("设置的卡号不符合规范")

def setMaxTZED():
    """
    设置最大的透支额度
    """
    set_dict = json.load(open(setting.SET_DIR_FILE, 'r'))
    print("现在最大透支额度为：", set_dict['max_ed'])
    userinput = input("输入需要设置的最大透支额度(%s 退出设置):" % QUIT_CHAR)
    if userinput == QUIT_CHAR:
        return False
    elif userinput.isdigit():
        userinput_int = int(userinput)
        if userinput_int > 0:
            set_dict['max_ed'] = userinput_int
            json.dump(set_dict, open(setting.SET_DIR_FILE, 'w'))
            print("设置成功")
            logging.info('%s 设置最大透支额度为 %s' % (USER_STATUS['LOGIN_USER_NAME'], userinput))
        else:
            print("输入不合法")
    else:
        print("输入不合法")


def main():
    print("进入主程序")
    main_flag = True
    while main_flag:
        print_str = """ --------主菜单----------
    1.设置最大透支额度
    2.添加用户
    3.设置用户额度
    4.冻结用户
    5.删除用户

    选择：数字   退出：%s
---------------------------
        """ % QUIT_CHAR
        print(print_str)
        User_Choose = input("请选择：")
        if User_Choose == QUIT_CHAR:
            print("退出")
            main_flag = False
            continue
        elif User_Choose.isdigit():
            User_Choose_int = int(User_Choose)
            if User_Choose_int <= 5:
                if User_Choose_int == 1:
                    setMaxTZED()
                elif User_Choose_int == 2:
                    addUser()
                elif User_Choose_int == 3:
                    setUserED()
                elif User_Choose_int == 4:
                    stopUser()
                elif User_Choose_int == 5:
                    delUser()
                else:
                    pass
            else:
                print("输入错误")
        else:
            print("输入不合法")


def login():
    """
    用户登录方法
    """
    while True:
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if os.path.exists(os.path.join(setting.ADMIN_DIR_FOLDER, username,)):
            user_dict = json.load(open(os.path.join(setting.ADMIN_DIR_FOLDER, username), 'r'))
            if username == user_dict['username'] and password == user_dict['password']:
                USER_STATUS['IS_LOGIN'] = True
                USER_STATUS['LOGIN_USER_NAME'] = username
                logging.info('%s 管理登录成功' % username)
                return True
            else:
                print('密码错误')
        else:
            print("用户不存在")


def run():
    """
    程序运行入口
    :return:
    """
    print("程序开始运行")
    if login():
        main()


if __name__ == '__main__':
    print(setting.ADMIN_DIR_FOLDER)
    run()
