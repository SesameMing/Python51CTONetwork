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


userdict = {}

print("Welcome System OS")
# username = input("username:")
# password = input("password:")


user_data = open('user.txt')
for i in user_data:
    userlist = i.strip()
    userdata = userlist.split(',')
    user_name = userdata[0].strip()
    user_passwd = userdata[1].strip()
    user_lock = userdata[2].strip()
    userdict[user_name] = {'username':user_name,'password':user_passwd,'lock':user_lock}

print(userdict)
user_data.close()





# if username == user and password == passwd:
#     print("Success!")
# else:
#     print("帐号密码错误")