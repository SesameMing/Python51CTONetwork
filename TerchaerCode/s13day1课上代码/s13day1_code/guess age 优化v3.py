#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
age = 22
for i in range(10):
    #i = 0
    print('new i2',i)
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
        #print("too many attempts...bye")
        #break
        continue_confirm = input("Do you want to continue because you are stupid:")
        if continue_confirm == 'y':
            #pass #
            i = 0
            print('new i',i)
        else:
            print("bye")
            break
