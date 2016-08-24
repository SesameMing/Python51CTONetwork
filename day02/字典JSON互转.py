#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-24 21:26

import json

'''
product_dict = {
    '手机类': {'name': '手机类',
        'product': {
           '小米3': {'name': '小米3',
               'price': 1299,
               'amout': 9999
              },
           '小米4': {'name': '小米4',
               'price': 1799,
               'amout': 9999
              },
           '小米5': {'name': '小米5',
               'price': 1999,
               'amout': 9999
              },
           'IPhone6 16G': {'name': 'IPhone6 16G',
               'price': 5288,
               'amout': 9999
              },
           'IPhone6 64G': {'name': 'IPhone6 64G',
               'price': '5888',
               'amout': 9999
              },
           'IPhone6S 16G': {'name': 'IPhone6S 16G',
               'price': 5888,
               'amout': 9999
              },
            'IPhone6S 64G': {'name': 'IPhone6S 64G',
               'price': 6888,
               'amout': 9999
              },
           '魅族 PRO': {'name': '魅族 PRO',
               'price': 1999,
               'amout': 9999
               },
        },
       },
    '汽车类': {
        'name': '汽车类',
        'product': {
            '宝马': {
                'name': '宝马',
                'price': 500000,
                'amout': 9999
            },
            '特斯拉': {
                'name': '特斯拉',
                'price': 820000,
                'amout': 9999

            }
        }
    }
}
'''
product_dict = {
    1: {'name': '手机类',
        'product': {
           1: {'name': '小米3',
               'price': 1299,
               'amout': 9999
              },
           2: {'name': '小米4',
               'price': 1799,
               'amout': 9999
              },
           3: {'name': '小米5',
               'price': 1999,
               'amout': 9999
              },
           4: {'name': 'IPhone6 16G',
               'price': 5288,
               'amout': 9999
              },
           5: {'name': 'IPhone6 64G',
               'price': '5888',
               'amout': 9999
              },
           6: {'name': 'IPhone6S 16G',
               'price': 5888,
               'amout': 9999
              },
           7: {'name': 'IPhone6S 64G',
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
            },
            2: {
                'name': '特斯拉',
                'price': 820000,
                'amout': 9999

            }
        }
    }
}





print(json.dump(product_dict,open('product.txt', 'w')))
d = json.load(open('product.txt','r'))
for k,v in enumerate(sorted(d)):

    print(v,d[v]['name'])