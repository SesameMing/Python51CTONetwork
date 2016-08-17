#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 23:40
#---------------
# 编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
#-----------------

user = 'SemaseMing'
passwd = '111111'


print("Welcome System OS")
username = input("username:")
password = input("password:")
i = 0

user_data = open('user.txt')
print(user_data)
user_data.close()
if username == user and password == passwd:
    print("Success!")
else:
    print("帐号密码错误")