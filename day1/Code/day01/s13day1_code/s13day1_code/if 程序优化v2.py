#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
user = 'alex'
passwd= 'alex3714'

username = input("username:")
password = input("password:")

if user == username and passwd == password:
    print("Welcome login")
else:
    print("Invalid username or password..")