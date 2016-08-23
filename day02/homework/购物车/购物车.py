#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-23 23:06

flag = True #循环标志
EXIT_CHAR = 'q' #退出字符
product_dict = {
    1:{'name':'手机类',
       'product':{
           1:{'name':'小米3',
              'price':1299,
              'amout':9999
              },
           2:{'name':'小米4',
              'price':1799,
              'amout':9999
              },
           3:{'name':'小米5',
              'price':1999,
              'amout':9999
              },
           4:{'name':'IPhone6 16G',
              'price':5288,
              'amout':9999
              },
           5:{'name':'IPhone6 64G',
              'price':'5888',
              'amout':9999
              },
           6:{'name':'IPhone6S 16G',
              'price':5888,
              'amout':9999
              },
           7:{'name': 'IPhone6S 64G',
               'price': 6888,
               'amout': 9999
              },
           8: {'name': '魅族 PRO',
               'price': 1999,
               'amout': 9999
               },
        },
       },
    2: {
        'name': '汽车类',
        'product': {
            1: {
                'name': '宝马',
                'price': 500000,
                'amout': 9999
            }
        }
    }
}
for key in product_dict:
    print(key,'.',product_dict[key]['name'])
