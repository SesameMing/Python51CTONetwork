#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

age = 22
guess_num = int( input("input your guess num:") )
if guess_num == age :
    print("Congratulations! you got it.")
elif guess_num >age:
    print("Think smaller!")
else:
    print("Think Big...")

