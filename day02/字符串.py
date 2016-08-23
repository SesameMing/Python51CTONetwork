#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-23 13:05



'''
#移除空白
username = input("user:")
if username.strip() == "Semase":
    print("welcome")

'''

'''
#分割和合并
name = "Semase,Ming"
name2 = name.split(',') #分割字符串
print(name2)
print("|".join(name2)) #合并字符串
print(name2)

'''
'''
name = "semase Ming"
print(" " in name) #判断有没有空格
print(name.capitalize()) #首字母大写
'''


msg = "Hello, {name}, it's been a long {age}  since last time sopke..."
msg2 = msg.format(name='Daming', age=22)
print(msg2)

msg3 = "hahahahahaha{0},ddddd{1}"
print(msg3.format('dming',22))


name = "Seamse Ming"
print(name.center(40,'-')) #
name.find('S')

age = input("your age")
age.isdigit()

