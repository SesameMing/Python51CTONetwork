#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-21 15:01

import os
import json
import time
from conf import setting
from modules.core.backend.loggingset import loger

QUIT_CHAR = 'q'  # 退出程序字符
USER_STATUS = {'IS_LOGIN': False, 'LOGIN_USER_CARDNAME': None}  # 用户登录状态
USER_PATH = ''

def huankuan():
    """
    还款
    """
    sum_money = 0
    userinfo = json.load(
        open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'], 'basic_info.json'), 'r'))
    print("---------信用卡账单----------")
    for item in userinfo['debt']:
        print("%s  %s  %s元" % (item['date'], item['info'], item['money']))
        sum_money += int(item['money'])
    print("本期共透支：%s 元" % sum_money)
    print("-----------账单结束----------")
    money = input("您需要还款<还款需要大于等于透支金额>: ")
    if money.isdigit():
        if int(money) < sum_money:
            print("还款金额小于透支总额")
        else:
            userinfo['debt'].clear()
            userinfo['balance'] = int(userinfo['balance']) + (int(money) - sum_money)
            userinfo['kycradit'] = userinfo['cradit']
            json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                                  'basic_info.json'), 'w'))
            msg = "卡号：%s 还款 - %s 元 - %s元存入余额 -成功" % (USER_STATUS['LOGIN_USER_CARDNAME'], money,
                                                     (int(money) - sum_money))
            logermsg.info(msg)

    else:
        print("金额格式不正确")

def chazhang():
    """
    查帐
    """
    sum_money = 0
    userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'], 'basic_info.json'), 'r'))
    print("---------信用卡账单----------")
    for item in userinfo['debt']:
        print("%s  %s  %s元" % (item['date'], item['info'], item['money']))
        sum_money += int(item['money'])
    print("本期共透支：%s 元" % sum_money)
    print("-----------账单结束----------")


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
        msg = "卡号：%s 修改密码 - 成功" % USER_STATUS['LOGIN_USER_CARDNAME']
        logermsg.info(msg)
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
----------------------------
    """ % (userinfo['balance'], userinfo['cradit'], userinfo['kycradit'])
    print(print_str)


def qukuan():
    """
    取款
    """
    money = input("请输入取款金额：")
    if money.isdigit():
        money_int = int(money)
        userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                               'basic_info.json'), 'r'))
        if money_int <= userinfo['balance']:
            """ 取款金额不大于存款余额的时候 直接扣除余额  """
            userinfo['balance'] -= money_int
            json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'], 
                                                  'basic_info.json'), 'w'))
            msg = "卡号：%s 取款 %s 元" % (USER_STATUS['LOGIN_USER_CARDNAME'], money_int)
            logermsg.info(msg)
        elif money_int <= (int(userinfo['balance']) + int(userinfo['kycradit'])):
            """ 取款金额不大于存款余额和可用信用额度 """
            xiaofeiedu = money_int - int(userinfo['balance'])
            userinfo['kycradit'] = int(userinfo['kycradit']) - xiaofeiedu
            print(userinfo['kycradit'])
            userinfo['balance'] = 0
            debt_list = {'date': time.strftime("%Y-%m-%d", time.localtime()), 'info': '取款额度', 'money': xiaofeiedu}
            userinfo['debt'].insert(0, debt_list)
            json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                        'basic_info.json'), 'w'))
            msg = "卡号：%s 取款 %s 元 - 成功" % (USER_STATUS['LOGIN_USER_CARDNAME'], money_int)
            logermsg.info(msg)

        else:
            """ 取款金额大于存款余额和可用信用额度 """
            print("您没有这么多的余额可以取款")
    else:
        print("输入的金额不合法")


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
            userinfo['balance'] = int(userinfo['balance']) + money_int
            json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                                  'basic_info.json'), 'w'))
            msg = "卡号：%s 存款 - %s 元 - 成功" % (USER_STATUS['LOGIN_USER_CARDNAME'], money_int)
            logermsg.info(msg)

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
        # zz_num_int = int(zz_num)
        if zz_num == USER_STATUS['LOGIN_USER_CARDNAME']:
            print("你不能自己给自己转账")
        elif os.path.exists(os.path.join(setting.USER_DIR_FOLDER, zz_num, 'basic_info.json')):
            zz_moeny = input("请输入转账金额：")
            if zz_moeny.isdigit():
                if int(zz_moeny) <= int(userinfo['balance']):
                    userinfo['balance'] = int(userinfo['balance']) - int(zz_moeny)
                    zz_dic = json.load(open(os.path.join(setting.USER_DIR_FOLDER, zz_num, 'basic_info.json'), 'r'))
                    zz_dic['balance'] = int(zz_dic['balance']) + int(zz_moeny)

                    json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'],
                                                          'basic_info.json'), 'w'))
                    json.dump(zz_dic, open(os.path.join(setting.USER_DIR_FOLDER, zz_num,
                                                          'basic_info.json'), 'w'))
                    print("转账成功")
                    msg = "卡号：%s 转账给 卡号：%s - %s 元 - 成功" % (USER_STATUS['LOGIN_USER_CARDNAME'], zz_num, zz_moeny)
                    logermsg.info(msg)

                else:
                    print("您没有这么多钱可以转")
            else:
                print("错误的转账格式")
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
            msg = "卡号：%s 退出登录" % USER_STATUS['LOGIN_USER_CARDNAME']
            logermsg.info(msg)
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
                if user_dic['status'] == 1:
                    USER_STATUS['IS_LOGIN'] = True
                    USER_STATUS['LOGIN_USER_CARDNAME'] = cardnum
                    return True
                else:
                    print("该卡号已被冻结,请联系管理员")
            else:
                print("密码错误")
        else:
            print("卡号错误,请检查后重新输入")


def run():
    print("欢迎登录ATM系统")
    if login():
        global USER_PATH
        global logermsg
        USER_PATH = os.path.join(setting.USER_DIR_FOLDER, USER_STATUS['LOGIN_USER_CARDNAME'], 'cardinfo', 'access.log')
        logermsg = loger(USER_PATH)
        msg = "卡号：%s 登录成功" % USER_STATUS['LOGIN_USER_CARDNAME']
        logermsg.info(msg)
        main()
