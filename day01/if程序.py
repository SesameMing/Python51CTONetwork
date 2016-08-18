#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 下午7:20

user = 'SemaseMing'
passwd = '111111'

username = input("username:")
passwrod = input("passwerd:")

if user == username:
    print("username is correct")
    if passwrod == passwd:
        print("Wellcome login...")
    else:
        print("password is invalid...")
else:
    print("连用户名都没有蒙对。滚粗。。。")