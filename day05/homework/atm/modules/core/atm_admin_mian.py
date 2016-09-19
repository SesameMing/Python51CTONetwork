#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-09-15 19:50
# atm程序主程序


import os
import json
from conf import setting
QUIT_CHAR = 'q'  # 退出程序字符
USER_STATUS = {'IS_LOGIN': False, 'LOGIN_USER_NAME': None}  # 用户登录状态


def delUser():
    """
    删除用户
    """


def stopUser():
    """
    冻结用户
    """


def setUserED():
    """
    设置用户额度
    """
    pass


def addUser():
    """
    添加用户
    """
    pass


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
            json.dump(set_dict,open(setting.SET_DIR_FILE, 'w'))
            print("设置成功")
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
        """ % (QUIT_CHAR)
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
