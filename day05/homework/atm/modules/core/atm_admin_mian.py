#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-15 19:50
# atm程序主程序




import os
import json
from conf import setting
QUIT_CHAR = 'q'
USER_STATUS = {'IS_LOGIN': False, 'LOGIN_USER_NAME': None}


def main():
    print("进入主程序")
    print_str = """ --------主菜单----------
1.设置最大透支额度
2.添加用户
3.设置用户额度
4.冻结用户
5.删除用户

选择：数字   退出：%s
---------------------------
    """ % (QUIT_CHAR)
    print(print_str)


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
    print(settings.ADMIN_DIR_FOLDER)
    run()
