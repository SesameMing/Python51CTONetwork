#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

USER_INFO = {}
# USER_INFO['is_login'] = True
# USER_INFO['user_type'] = 2

def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print('请登录')
    return inner

def check_admin(func):
    def inner():
        if USER_INFO.get('user_type', None) == 2:
            ret = func(1121121)
            return ret
        else:
            print('无权限查看')

    return inner

@check_admin
def index(a):
    """
    管理员的功能
    :return:
    """
    print('Index')

index()

