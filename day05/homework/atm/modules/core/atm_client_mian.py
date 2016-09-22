#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-21 15:01

import os
import json
from conf import setting
QUIT_CHAR = 'q'  # 退出程序字符
USER_STATUS = {'IS_LOGIN': False, 'LOGIN_USER_CARDNAME': None}  # 用户登录状态


def huankuan():
    """
    还款
    """


def chazhang():
    """
    查帐
    """


def xiugaimima():
    """
    修改密码
    """
    old_password = input("请输入旧密码：")
    userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                           'basic_info.json'), 'r'))
    if old_password == userinfo['password']:
        new_password = input("请输入新密码：")
        userinfo['password'] = new_password
        json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                              'basic_info.json'), 'w'))
        print("修改成功")
    else:
        print("密码输入错误")


def chaxun():
    """
    查询
    """
    userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                           'basic_info.json'), 'r'))
    print_str = """ -------- 查询结果 ---------
    余额    ：%s 元
    信用额度 ：%s 元
    可用额度 ：%s 元
------------------------
    """ % (userinfo['balance'], userinfo['cradit'], userinfo['kycradit'])
    print(print_str)


def qukuan():
    """
    取款
    """


def cunqian():
    """
    存钱
    """
    money = input("请输入您要存款的金额：")
    if money.isdigit():
        money_int = int(money)
        if money_int > 0:
            userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                                   'basic_info.json'), 'r'))
            userinfo['balance'] = money_int
            json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                                  'basic_info.json'), 'w'))
            print("存钱成功")

        pass
    else:
        print("错误的存入金额数")


def zhuangzhan():
    """
    转账
    """
    userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                           'basic_info.json'), 'r'))
    print("您的可用余额为：%s 元" % userinfo['balance'])
    zz_num = input("请输入对方卡号：")
    if zz_num.isdigit():
        zz_num_int = int(zz_num)
        if zz_num_int == USER_STATUS['LOGIN_USER_CARDNAME']:
            print("你不能自己给自己转账")
        elif os.path.exists(os.path.join(setting.USER_DIR_FOLDER, zz_num_int)):
            pass
        else:
            print("转账用户不存在")
    else:
        print("错误的帐号格式")


def main():
    print("主程序")
    main_flat = True
    while main_flat:
        mian_str = """-----------主菜单----------
1.转账
2.存钱
3.取款
4.查询
5.修改密码
6.查账
7.还款

    选择：数字   退出：%s
---------------------------
        """ % QUIT_CHAR
        print(mian_str)
        userchose = input("请输入您的选择：")
        if userchose == QUIT_CHAR:
            print("退出程序")
            USER_STATUS['IS_LOGIN'] = True
            main_flat = False
            continue
        elif userchose.isdigit():
            userchose_int = int(userchose)
            if userchose_int <= 7:
                userchose_int = int(userchose)
                if userchose_int == 1:
                    zhuangzhan()
                elif userchose_int == 2:
                    cunqian()
                elif userchose_int == 3:
                    qukuan()
                elif userchose_int == 4:
                    chaxun()
                elif userchose_int == 5:
                    xiugaimima()
                elif userchose_int == 6:
                    chazhang()
                elif userchose_int == 7:
                    huankuan()
                else:
                    pass

            else:
                print("输入不合法,不在范围内")
        else:
            print("输入不合法")


def login():
    while True:
        cardnum = input("请输入卡号：")
        if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, cardnum)):
            user_dic = json.load(open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json')))
            password = input("请输入密码：")
            if password == user_dic['password']:
                print("密码正确")
                USER_STATUS['IS_LOGIN'] = True
                USER_STATUS['LOGIN_USER_CARDNAME'] = cardnum
                return True
            else:
                print("密码错误")
        else:
            print("卡号错误,请检查后重新输入")


def run():
    print("欢迎登录ATM系统")
    if login():
        main()
