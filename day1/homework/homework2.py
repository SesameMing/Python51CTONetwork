#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-17 22:23

# 三级菜单。
# b：返回上一级 q:退出整个程序

ones_menu = {} #一级菜单
two_menu = {} #二级菜单
three_menu={} #三级菜单

#还是一个总的菜单呢
menu_list = {'中国':{'北京':{'北京-直辖市'},'上海':['上海直辖市'],'湖北':['武汉','宜昌'],'广东':{'广州','深圳','东莞'}},'其他国家':{'其他国家省份/州':"其他国家城市/地区"}}
cengji = 0

menu = menu_list.keys()
while True:
    for i in (range(menu)):
        print(i)
    userchooes = input("请输入您的选择")