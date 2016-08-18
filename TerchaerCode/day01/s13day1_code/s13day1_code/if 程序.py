#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
user = 'alex'
passwd= 'alex3714'

username = input("username:")
password = input("password:")

if user == username:
    print("username is correct...")
    if password == passwd:
        print("Welcome login .....")
    else:
        print("password is invalid...")
else:
    print("连用户名都 没蒙对，滚粗。。。")