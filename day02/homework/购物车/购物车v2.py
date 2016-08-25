#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-23 23:06

import os
import json
import time


flag_user_login = True  # 用户登录
flag_one = False        # 循环标志
EXIT_CHAR = 'q'         # 退出字符
CAR_CHAR = 'c'          # 进入购物车字段
RECHARGE_CHAR = 'p'     # 进入充值
USERFILE = 'user.txt'   # 用户配置文件名称
PRODUCTFILE = 'product.txt'  # 产品配置文件名称
REEOR_NUM = 3           # 允许错误次数
userdict = {}           # 初始化用户数据字典
# login_username = ''     # 存储登录用户名称

tip_str = "[%s = 退出， %s = 购物车 %s = 充值] " % (EXIT_CHAR, CAR_CHAR, RECHARGE_CHAR)

# 购物车方法
def shopcar():
    print("购物车".center(40, '-'))
    print(flag_user_login)
    print("结束".center(40, '-'))
# 充值方法
def recharge():
    print(username)
    print("充值系统".center(40, '-'))

# 修改保存用户数据文件
def w_userfiel():
    wirte_data = open(USERFILE, 'w+')
    for t in userdict.values():
        wuserdata = [t['username'], t['password'], str(t['lock']), str(t['errornum']), str(t['balance']), '\n']
        wuserdatestr = ','.join(wuserdata)
        wirte_data.write(wuserdatestr)
    wirte_data.close()


# 主程序开始
# 判断配置文件是否存在（用户登录文件）
print("正在加载配置文件")
time.sleep(1)
if os.path.exists(USERFILE) and os.path.exists(PRODUCTFILE):
    product_dict = json.load(open(PRODUCTFILE, 'r'))
    print("配置文件加载成功...")
    time.sleep(1)
else:
    exit("配置文件丢失，请检查程序完整性...")

while flag_user_login:
    print("欢迎来到【Python】商店".center(40, '-'))
    username = input("帐号：")
    password = input("密码：")
    user_data = open(USERFILE)
    for data in user_data:
        userlist = data.strip()
        userdata = userlist.split(',')
        user_name = userdata[0].strip()            # 用户名
        user_passwd = userdata[1].strip()          # 密码
        user_lock = userdata[2].strip()            # 是否锁定
        user_error_num = int(userdata[3].strip())  # 错误次数
        user_balance = int(userdata[4].strip())    # 用户余额
        userdict[user_name] = {'username': user_name, 'password': user_passwd, 'lock': user_lock,
                               'errornum': user_error_num, 'balance': user_balance}
    user_data.close()

    # 判断用户登录的合法性
    if username in userdict.keys():
        if userdict[username]['lock'] == '1':
            print('\033[31;1m提示：\033[0m该账户已被锁定,请联系管理员')
            flag_user_login = False
            continue
        if username == userdict[username]['username'] and password == userdict[username]['password']:
            print("Success! 登录成功，欢迎%s 您的余额为%d" % (username, userdict[username]['balance']))
            flag_one = True
        else:
            userdict[username]['errornum'] += 1
            if userdict[username]['errornum'] >= REEOR_NUM:
                print('帐号密码输入错误%d次，被锁定，退出' % REEOR_NUM)
                userdict[username]['lock'] = 1
                userdict[username]['errornum'] = 0
                flag_user_login = False
            else:
                print('帐号密码错误')
            w_userfiel()
        while flag_one:
            flag_two = True  # 二层循环标志
            for val in sorted(product_dict):
                print(val, '.', product_dict[val]['name'])
            num1 = input(tip_str + "请输入您需要的物品分类id：")
            if num1.isdigit():
                if int(num1) <= len(product_dict):
                    while flag_two:
                        # 产品列表循环 开始
                        print(product_dict[num1]['name'].center(40, '-'))
                        print('id', '产品名称'.ljust(15, ' '), '单价'.ljust(10, ' '), '库存'.ljust(10, ' '))
                        for v in sorted(product_dict[num1]['product']):
                            print(str(v), '.', product_dict[num1]['product'][v]['name'].ljust(15, ' '),
                                  str(product_dict[num1]['product'][v]['price']).ljust(10, ' '),
                                  str(product_dict[num1]['product'][v]['amout']).ljust(10, ' '))
                        print('列表结束'.center(40, '-'))
                        # 产品列表徐欢 结束
                        num2 = input(tip_str + "请输入您需要的物品分类id：")
                        if num2.isdigit():
                            if int(num2) < len(product_dict[num1]['product']):
                                product_num = input("请输入您要购买的%s的数量：" %
                                                    product_dict[num1]['product'][num2]['name'])
                                userdict[username]['balance'] -= product_dict[num1]['product'][num2]['price'] * int(product_num)

                                # 1.需要将购买记录写入到文件  START

                                # 1.需要将购买记录写入到文件  END

                                # 2.需要将用户余额写入到文件  START
                                w_userfiel()
                                # 2.需要将用户余额写入到文件 END
                                print('购买成功', product_dict[num1]['product'][num2]['name'],
                                      '数量：', product_num, '您的余额为', userdict[username]['balance'])

                            else:
                                print("超出选择范围，请重新选择")
                        else:
                            if num2 == EXIT_CHAR:
                                print("退出程序")
                                flag_one = False
                            elif num2 == CAR_CHAR:
                                shopcar()
                                continue
                            elif num2 == RECHARGE_CHAR:
                                recharge()
                                continue

                else:
                    print("超出选择范围,请重新选择")
            else:
                if num1 == EXIT_CHAR:
                    print("退出程序")
                    flag_one = False
                elif num1 == CAR_CHAR:
                    shopcar()
                    continue
                elif num1 == RECHARGE_CHAR:
                    recharge()
                    continue

    else:
        print("帐号密码错误")

