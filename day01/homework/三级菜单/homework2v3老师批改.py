#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-17 22:23

# 三级菜单。
# b：返回上一级 q:退出整个程序 y:到第一级

# 还是一个总的菜单呢
'''
1、尽量不要用break语句退出while循环，这样会使得代码可读性下降，不好控制容易出错
而且三个循环都用flag一个变量控制？
为什么不三层循环用三个变量控制，这样可以自由对退出或进入某层循环，也可以摆脱break
'''
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
flag = True
QUIT = "q" #退出字符
LAST = "b" #上一层字符
DYC = "y" #返回到第一层
print("欢迎来到菜单选择 %s：退出 %s：返回上一层 %s: 返回到第一层" % (QUIT, LAST, DYC))
#第一层循环
while flag:
    sc = True
    for i in menu_list:
        print(i, '.', menu_list[i]['name'])
    num_1 = input("请输入一级菜单号:")
    if num_1==QUIT:
        print("退出程序")
        flag = False
        break
    elif num_1 == LAST:
        print("第一层没有上一级")
        continue
    elif num_1 == DYC:
        print("这就是第一层拉")
    elif num_1.isdigit():
        num_int_1 = int(num_1)
        if num_int_1 <= len(menu_list):
            #第二层循环
            while flag:
                if sc == False:
                    break
                for k in menu_list[num_int_1]['info']:
                    print(k,'.',menu_list[num_int_1]['info'][k]['name'])
                num_2 = input("请输入二级菜单:")
                if num_2==QUIT:
                    print("退出程序")
                    flag = False
                    break
                elif num_2 == LAST:
                    break
                elif num_2 == DYC:
                    sc = False
                    continue
                elif num_2.isdigit():
                    num_int_2 = int(num_2)
                    if num_int_2 <= len(menu_list[num_int_1]['info']):
                        #第三层循环
                        while flag:
                            if sc == False:
                                break
                            for l in menu_list[num_int_1]['info'][num_int_2]['info']:
                                print(l, '.', menu_list[num_int_1]['info'][num_int_2]['info'][l]['name'],menu_list[num_int_1]['info'][num_int_2]['info'][l]['info'])
                            num_3 = input("请输入菜单:")
                            if num_3 == QUIT:
                                print("退出程序")
                                flag = False
                                break
                            elif num_3 == LAST:
                                break
                            elif num_3 == DYC:
                                sc = False
                                continue
                            elif num_3.isdigit():
                                print("这已经是最后一层菜单，请其他选择 %s：退出 %s：返回上一层 %s: 返回到第一层"% (QUIT, LAST, DYC))
                    else:
                        print('错误的数字编号输入,请重新输入')
        else:
            print('错误的数字编号输入')
    else: # 第一层的退到第一层
        pass


