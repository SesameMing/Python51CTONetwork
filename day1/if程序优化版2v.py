#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 下午7:20

user = 'SemaseMing'
passwd = '111111'

username = input("username:")
passwrod = input("passwerd:")

if user == username and passwrod ==passwd:
    print("Welcome login")

else:
    print("Invalid username or password")