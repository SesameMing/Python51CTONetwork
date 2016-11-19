#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")

welcome_msg = 'Welcome to Alex Shopping mall'.center(50,'-')
print(welcome_msg)

exit_flag = False
product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi 2',19.9),
    ('Coffee',30),
    ('Tesla',820000),
    ('Bike',700),
    ('Cloth',200),]

shop_car = []
while  exit_flag is not True:
    #for product_item in product_list:
    #    p_name,p_price = product_item
    print("product list".center(50,'-'))
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)

    user_choice = input("[q=quit,c=check]What do you want to buy?:")
    if user_choice.isdigit():#肯定是选择shangpin
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary: #买的起
                shop_car.append(p_item) #放入购物车
                salary -= p_item[1] #减钱
                print("Added [%s] into shop car,you current balance is \033[31;1m[%s]\033[0m" %
                      (p_item,salary))
            else:
                print("Your balance is [%s],cannot afford this.." % salary)
    else:
        if user_choice == 'q' or user_choice =='quit':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is [%s]" % salary)
            print("Bye")
            exit_flag = True
        elif  user_choice == 'c' or user_choice =='check':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)

