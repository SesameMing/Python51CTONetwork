#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-17 22:23

# 三级菜单。
# b：返回上一级 q:退出整个程序 y:到第一级
'''
相比第一个作业，这个完全不符合要求
几个大问题得说一下
1、deepcopy这个东西最好不要用
我个人认为这是违背python的简洁高效的，非常消耗资源的。
python之所以将相同的字典列表等指向同一块内存空间是有他的道理的
deepcopy是需要重新开辟内存空间的消耗资源不说，效率还非常低
2、shurulist = ['1','2','3','4','5','6','7','8','9','q','b','y']
这个完全没有必要这么做，完全可以通过字典的has_key或者in方法来判断
3、按照作业的考察点，这里每一级都应该是一层循环
4、应尽量少用break退出循环，break在多层循环中会是的逻辑非常不清晰，并且不好控制
'''
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