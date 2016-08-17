#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 下午7:39

age = 21
for i in range(10):
    if i < 3:
        guess_num = int(input("input your guess num:"))
        if guess_num == age:
            print("Congratulations! you got it.")
            break
        elif guess_num > age:
            print("Think smaller!")
        else:
            print("Think Big...")
    else:
        print("too many attrempts... bye")