#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
age = 22
for i in range(10):
    if i <3:
        guess_num = int( input("input your guess num:") )
        if guess_num == age :
            print("Congratulations! you got it.")
            break #不往后走了，跳出整 个loop
        elif guess_num >age:
            print("Think smaller!")
        else:
            print("Think Big...")
    else:
        print("too many attempts...bye")
        break

