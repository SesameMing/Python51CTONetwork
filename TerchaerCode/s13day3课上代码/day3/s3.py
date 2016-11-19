#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li


def login(username, password):
    """
    用于用户登录
    :param username: 用户输入的用户名
    :param password: 用户输入的密码
    :return: true，表示登录成功；false，登录失败
    """
    f = open("db", 'r')
    for line in f:
        line_list = line.strip().split("|")
        if line_list[0] == username and line_list[1] == password:
            return True
    return False


def register(username, password):
    """
    用于用户注册
    :param username: 用户名
    :param password: 密码
    :return: 默认None
    """
    f = open("db", 'a')
    temp = "\n" + username + "|" + password
    f.write(temp)
    f.close()


def main():
    t = input("1：登录；2：注册")
    if t == "1":
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        r = login(user, pwd)
        if r:
            print("登录成功")
        else:
            print("登录失败")
    elif t == "2":
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        register(user, pwd)

main()
