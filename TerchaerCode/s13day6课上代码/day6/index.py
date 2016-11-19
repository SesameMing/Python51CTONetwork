#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li


# def run():
#     inp = input('请输入要访问的url:')
#     if inp == 'login':
#         commons.login()
#     elif inp == 'logout':
#         commons.logout()
#     elif inp == 'home':
#         commons.home()
#     else:
#         print('404')
# import commons as obj
# obj.login()
#
# obj = __import__("commons")
# obj.login()
# # import "commons"
# import account
# import manager

def run():
    # account/login
    inp = input('请输入要访问的url:')
    # inp字符串类型 inp = "login"
    # commons.inp() # commons.login
    # 利用字符串的形式去对象（模块）中操作（寻找/检查/删除/设置）成员，反射

    m, f = inp.split('/')
    # import lib.account
    obj = __import__("lib."+ m, fromlist=True)
    if hasattr(obj, f):
        func = getattr(obj, f)
        func()
    else:
        print('404')

if __name__ == '__main__':
    run()