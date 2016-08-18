#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-17 22:23

# 三级菜单。
# b：返回上一级 q:退出整个程序 y:到第一级

import copy

# 还是一个总的菜单呢
menu_list = {
    1: {
        'name': '中国'
        , 'info': {
            1: {
                'name': '北京',
                'info': {
                    1: {
                        'name': '北京市',
                        'info': '北京是中国的首都'
                    }
                }
            },
            2: {
                'name': '上海',
                'info': {
                    1: {
                        'name': '上海市',
                        'info': '上海是一个非常有魅力的地方，我想去的地方'
                    }
                }
            }
        }
    },
    2: {
        'name': '美国',
        'info': {
            1: {
                'name': '加州',
                'info': {
                    1: {
                        'name': '洛杉矶',
                        'info': '天使之城'
                    },
                    2: {
                        'name': '旧金山',
                        'info': '旧金山唐人街'
                    }
                }
            }
        }
    }
}
menu_tmp = {} #初始化临时meun
menu = copy.deepcopy(menu_list) #拷贝菜单
menu_last = {} #初始化上级菜单
cengji = 0 #初始化层级
choose = 0 #初始化输入
z = '' #初始化字符串
shurulist = ['1','2','3','4','5','6','7','8','9','q','b','y'] #允许输入的字符列表


print("欢迎来到级菜单")
print("提示：数字:进入下一级别 b:返回上一级 y:返回第一级 q:退出")
while True:
    #print('现在的层级为：',cengji)
    for i in menu:
        print(i, '.', menu[i]['name'])
    choose = input('请输入您的选择:')
    if choose not in shurulist:
        print('您的输入不在范围之内,请重新输入')
        continue
    if choose == 'q':
        print('退出')
        break
    elif choose == 'b':
        print('返回上一级')
        cengji -= 1
        if cengji==0:
            menu = copy.deepcopy(menu_list)
        else:
            menu = copy.deepcopy(menu_last)
        continue
    elif choose == 'y':
        print('返回第一层')
        menu = copy.deepcopy(menu_list)
        cengji = 0
        continue
    elif (int(choose) in menu):
        cengji += 1
    else:
        print('您的输入不在范围之内')
        continue

    if cengji <= 0:
        print('这已经是第一层了,不能再上一层了,请重新选择')
        cengji += 1
        continue
    elif cengji == 1:
        pass
    elif cengji == 2:
       pass
    elif cengji >= 3:
        print('这已经是最后一级菜单了，请重新选择其他操作')
        cengji = 2
        continue

    menu_last = copy.deepcopy(menu)
    menu_tmp = menu[int(choose)]['info']
    menu.clear()
    menu = menu_tmp