#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

import getpass
username = input("username:")
password = getpass.getpass("password:")
print(username,password)

import  os

os.system('df')
os.mkdir('yourDir')
cmd_res = os.popen("df -h").read()

import sys
print(sys.path)
#'/usr/lib/python2.7/dist-packages' 自己写的模块

