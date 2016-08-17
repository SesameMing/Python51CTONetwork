#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 下午7:39

age = 21
counter = 0
for i in range(10):
    if counter < 3:
        guess_num = int(input("input your guess num:"))
        if guess_num == age:
            print("Congratulations! you got it.")
            break
        elif guess_num > age:
            print("Think smaller!")
        else:
            print("Think Big...")
    else:
       continue_confirm = input("Do you want to contiune beacuse you are stupid(y/n):")
       if continue_confirm == 'y':
           counter = 0
           continue
       else:
           print("bey")
           break


    counter += 1