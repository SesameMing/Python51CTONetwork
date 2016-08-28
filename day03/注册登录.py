#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-28 19:09


def login(username, password):
    """
    用于用户登录
    :param username: 用户输入的用户名
    :param password: 用户输入的密码
    :return: true,表示登录成功；false，表示登录失败
    """
    file = open('db', 'r')
    for f in file:
        f_list = f.strip().split('|')
        if username == f_list[0] and password == f_list[1]:
            return True
    return False


def register(username, password):
    """
    用于用户注册
    :param username: 注册用户名
    :param password: 注册密码
    :return: None
    """
    file = open('db', 'a')
    temp = '|'.join([str(username), str(password), '\n'])
    file.write(temp)
    file.close()


def main():
    t = input("1:登录； 2：注册")
    if t == '1':
        print('登录')
        user = input("请输入用户名：")
        passwd = input("请输入密码：")
        r = login(user, passwd)
        if r:
            print('登录成功')
        else:
            print('登录失败')
    elif t == '2':
        print('注册')
        user = input("请输入注册用户名：")
        passwd = input("请输入注册密码：")
        register(user, passwd)


main()
