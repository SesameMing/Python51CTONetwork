#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-23 23:06
'''
总的说来，非常不错，good
没有再犯之前的毛病
但是有一点有点强买强卖的意思，加入购物车的东西就不能反悔啊，
而且加入购物车就一定要买啊，哈哈哈哈哈哈哈，还么有投诉的地方，小心明年的315曝光你
'''


import os
import json
import time


flag_user_login = True  # 用户登录
flag_one = False        # 循环标志
EXIT_CHAR = 'e'         # 退出登录字符
QUIT_CHAR = 'q'         # 退出登录字符
CAR_CHAR = 'c'          # 进入购物车字段
RECHARGE_CHAR = 'p'     # 进入充值
LAST_CHAR = 'b'         # 返回上一级
HISTORY_CHAR = 'h'      # 历史购买记录
USERFILE = 'user.txt'   # 用户配置文件名称
PRODUCTFILE = 'product.txt'  # 产品配置文件名称
PAYFILE = 'pay.txt'     # 购买记录配置文件
REEOR_NUM = 3           # 允许错误次数
userdict = {}           # 初始化用户数据字典
ons_pay_history= []     # 本次购记录

tip_str = "[%s：购物车 %s：充值 %s：历史 %s：返回上一级 %s：退出登录 %s：退出系统] " % (CAR_CHAR, RECHARGE_CHAR, HISTORY_CHAR, LAST_CHAR, QUIT_CHAR, EXIT_CHAR)

# 修改保存用户数据文件
def w_userfiel():
    wirte_data = open(USERFILE, 'w+')
    for t in userdict.values():
        wuserdata = [t['username'], t['password'], str(t['lock']), str(t['errornum']), str(t['balance']), '\n']
        wuserdatestr = ','.join(wuserdata)
        wirte_data.write(wuserdatestr)
    wirte_data.close()

# 保存购买记录
def save_pay_history():
    payfile = open(PAYFILE,'a');
    wpaydata = ','.join(pay_list)
    payfile.write(wpaydata)
    payfile.close()

# 更新产品
def update_product_file():
    json.dump(product_dict, open(PRODUCTFILE, 'w'))


# 历史购物方法
def get_pay_history():
    payfile = open(PAYFILE)
    print("历史购买记录".center(40, '-'))
    print('产品名称'.ljust(7, ' '), '单价'.center(5, ' '), '数量'.center(5, ' '),'总价'.center(5,' '),'购买时间'.center(15, ' '))
    for i in payfile:
        paylist = i.strip()
        paylistdata = paylist.split(',')
        # pay_name = paylistdata[0].strip()
        if paylistdata[0].strip() == username:
            pay_product_name = paylistdata[1].strip()
            pay_product_price = int(paylistdata[2].strip())
            pay_product_num = int(paylistdata[3].strip())
            pay_product_sumprice = int(paylistdata[4].strip())
            pay_time = paylistdata[5].strip()
            print(pay_product_name.ljust(13, ' '), str(pay_product_price).ljust(10, ' '), str(pay_product_num).ljust(5, ' '),
                  str(pay_product_sumprice).ljust(10, ' '), pay_time)

    print("结束".center(40, '-'))
    input("请输入任意字符继续：")

# 本次登录的购物车
def one_pay_list():
    print("购物车".center(40, '-'))
    print('产品名称'.ljust(7, ' '), '单价'.center(5, ' '), '数量'.center(5, ' '), '总价'.center(5, ' '), '购买时间'.center(15, ' '))
    if ons_pay_history:
        for k in ons_pay_history:
            print(k[1].ljust(13, ' '), str(k[2]).ljust(10, ' '), str(k[3]).ljust(5, ' '),
              str(k[4]).ljust(10, ' '), k[5])
    else:
        print('购物车为空')
    print("购物车END".center(40, '-'))
    input("请输入任意字符继续：")

# 充值方法
def recharge():
    print("充值系统".center(40, '-'))
    money = input("请输入充值金额：")
    if money.isdigit():
        if int(money) > 0:
            userdict[username]['balance'] += int(money)
            w_userfiel()
            print("充值成功，您的余额为%d" % userdict[username]['balance'])
            return True
        else:
            print("充值金额不能为负数")
            return False
    else:
        if money == EXIT_CHAR:
            print("退出程序")
            flag_one = False
        elif money == CAR_CHAR:
            get_pay_history()
        elif money == RECHARGE_CHAR:
            recharge()
        elif money == LAST_CHAR:
            return False
        else:
            print("错误的充值金额，退出")
# 主程序开始
# 判断配置文件是否存在（用户登录文件）
print("正在加载配置文件")
# time.sleep(1)
if os.path.exists(USERFILE) and os.path.exists(PRODUCTFILE):
    product_dict = json.load(open(PRODUCTFILE, 'r'))
    print("配置文件加载成功...")
    # time.sleep(1)
else:
    exit("配置文件丢失，请检查程序完整性...")

while flag_user_login:
    ons_pay_history = []  # 本次购记录

    print('-' * 40)
    print('欢迎来到【Python】商店'.center(25, ' '))
    print('-' * 40)

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
            print("\033[32;1mSuccess! 登录成功\033[0m，欢迎%s 您的余额为%d" % (username, userdict[username]['balance']))
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

            print('产品分类'.center(40, '-'))
            print(tip_str.center(30, ' '))
            print('-'*45)

            for val in sorted(product_dict):
                print(val, '.', product_dict[val]['name'])
            # num1 = input(tip_str + "请输入您需要的物品分类id：")
            num1 = input("请输入您需要的物品分类id：")
            if num1.isdigit():
                if int(num1) <= len(product_dict):
                    while flag_two:
                        # 产品列表循环 START
                        print(product_dict[num1]['name'].center(40, '-'))
                        print(tip_str.center(30, ' '))
                        print('-' * 45)
                        print('id', '产品名称'.ljust(15, ' '), '单价'.ljust(10, ' '), '库存'.ljust(10, ' '))

                        for v in sorted(product_dict[num1]['product']):
                            print(str(v), '.', product_dict[num1]['product'][v]['name'].ljust(15, ' '),
                                  str(product_dict[num1]['product'][v]['price']).ljust(10, ' '),
                                  str(product_dict[num1]['product'][v]['amout']).ljust(10, ' '))
                        print('列表结束'.center(40, '-'))
                        # 产品列表徐欢 END
                        # num2 = input(tip_str + "请输入您需要的物品分类id：")
                        num2 = input("请输入您需要的物品id：")
                        if num2.isdigit():
                            if int(num2) <= len(product_dict[num1]['product']):
                                product_num = input("请输入您要购买的%s的数量：" %
                                                    product_dict[num1]['product'][num2]['name'])
                                if product_num.isdigit():
                                    if int(product_num) > 0 and int(product_num) <= product_dict[num1]['product'][num2]['amout']:
                                        sum_price = int(product_dict[num1]['product'][num2]['price']) * int(product_num)
                                        if userdict[username]['balance'] >= sum_price:
                                            userdict[username]['balance'] -= int(sum_price)
                                            # 1.需要将购买记录写入到文件  START  完成
                                            pay_list = [username, product_dict[num1]['product'][num2]['name'],
                                                        str(product_dict[num1]['product'][num2]['price']), product_num, str(sum_price),
                                                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n']
                                            ons_pay_history.append(pay_list)
                                            save_pay_history()
                                            # 2.更新用户余额并写入到文件  START  完成
                                            w_userfiel()
                                            # 3.更新产品的数量并文件 START  完成
                                            product_dict[num1]['product'][num2]['amout'] -= int(product_num)
                                            update_product_file()
                                            print('购买成功', product_dict[num1]['product'][num2]['name'],
                                                  '数量：', product_num, '您的余额为', userdict[username]['balance'])
                                        else:
                                            print("您的余额不足以支付本次购买，请及时充值")
                                    else:
                                        print("您输入的数字超出了范围")

                                else:
                                    print("超出选择范围，请重新选择")
                            else:
                                print("超出选择范围，请重新选择")
                        else:
                            if num2 == QUIT_CHAR:
                                one_pay_list()
                                print("退出登录")
                                flag_one = False
                                flag_two = False
                            elif num2 == EXIT_CHAR:
                                one_pay_list()
                                print("退出系统")
                                exit(0)
                            elif num2 == CAR_CHAR:
                                one_pay_list()
                                continue
                            elif num2 == HISTORY_CHAR:
                                get_pay_history()
                                continue
                            elif num2 == RECHARGE_CHAR:
                                recharge()
                                continue
                            elif num2 == LAST_CHAR:
                                flag_two = False
                                print("返回上一级")
                                continue
                            else:
                                print("错误的输入")

                else:
                    print("超出选择范围,请重新选择")
            else:
                if num1 == QUIT_CHAR:
                    one_pay_list()
                    print("退出登录")
                    flag_one = False
                elif num1 == EXIT_CHAR:
                    one_pay_list()
                    print("退出系统")
                    exit(0)
                elif num1 == CAR_CHAR:
                    one_pay_list()
                    continue
                elif num1 == HISTORY_CHAR:
                    get_pay_history()
                    continue
                elif num1 == RECHARGE_CHAR:
                    recharge()
                    continue
                elif num1 == LAST_CHAR:
                    flag_two = False
                    print("这是第一级啦，不能再上一级拉")
                    continue

    else:
        print("帐号密码错误")

