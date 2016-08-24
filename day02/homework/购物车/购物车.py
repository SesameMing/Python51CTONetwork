#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-23 23:06

import os


flag_user_login = True  # 用户登录
flag_one = False        # 循环标志
EXIT_CHAR = 'q'         # 退出字符
CAR_CHAR = 'c'          # 进入购物车字段
RECHARGE_CHAR = 'p'     # 进入充值
USERFILE = 'user.txt'   # 配置文件名称
REEOR_NUM = 3           # 允许错误次数
userdict = {}           # 初始化用户数据字典

tip_str = "[%s = 退出， %s = 购物车 %s = 充值] " % (EXIT_CHAR, CAR_CHAR, RECHARGE_CHAR)
product_dict = {
    1: {'name': '手机类',
        'product': {
           1: {'name': '小米3',
               'price': 1299,
               'amout': 9999
              },
           2: {'name': '小米4',
               'price': 1799,
               'amout': 9999
              },
           3: {'name': '小米5',
               'price': 1999,
               'amout': 9999
              },
           4: {'name': 'IPhone6 16G',
               'price': 5288,
               'amout': 9999
              },
           5: {'name': 'IPhone6 64G',
               'price': '5888',
               'amout': 9999
              },
           6: {'name': 'IPhone6S 16G',
               'price': 5888,
               'amout': 9999
              },
           7: {'name': 'IPhone6S 64G',
               'price': 6888,
               'amout': 9999
              },
           8: {'name': '魅族 PRO',
               'price': 1999,
               'amout': 9999
               },
        },
       },
    2: {
        'name': '汽车类',
        'product': {
            1: {
                'name': '宝马',
                'price': 500000,
                'amout': 9999
            },
            2: {
                'name': '特斯拉',
                'price': 820000,
                'amout': 9999

            }
        }
    }
}

# 购物车方法
def shopcar():
    print("购物车".center(40, '-'))
    print(flag_user_login)
    print("结束".center(40, '-'))
# 充值方法
def recharge():
    print("充值系统".center(40,'-'))

# 主程序开始
# 判断配置文件是否存在（用户登录文件）
if os.path.exists(USERFILE):
    print("配置文件加载成功...")
else:
    exit("配置文件丢失，请检查程序完整性...")

while flag_user_login:
    print("欢迎来到【Python】商店".center(40,'-'))
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
            print("Success! 登录成功，欢迎%s 您的余额为%d" % (username,userdict[username]['balance']))
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
            wirte_data = open(USERFILE, 'w+')
            for t in userdict.values():
                wuserdata = [t['username'], t['password'], str(t['lock']), str(t['errornum']), str(t['balance']),'\n']
                wuserdatestr = ','.join(wuserdata)
                wirte_data.write(wuserdatestr)
            wirte_data.close()
        while flag_one:
            for key in product_dict:
                print(key, '.', product_dict[key]['name'])
            num1 = input(tip_str + "请输入您需要的物品序号：")
            if num1.isdigit():
                pass
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

