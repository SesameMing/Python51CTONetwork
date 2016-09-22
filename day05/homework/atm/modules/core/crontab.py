#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-22 20:38
""" 自动执行脚本用来检查出账单的 """

import os
import json
import time
from conf import setting


def mian():
        struct_time = time.localtime()
        if struct_time.tm_mday == 9:
            cardlist  = os.listdir(setting.USER_DIR_FOLDER)
            for cardnum in cardlist:
                userinfo = json.load(open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json'), 'r'))
                sum_money = 0
                for item in userinfo['debt']:
                    sum_money += int(item['money'])
                if int(userinfo['balance']) >= sum_money:
                    """ 如果余额大于账单就自动还款 """
                    userinfo['balance'] = int(userinfo['balance']) - sum_money
                    userinfo['kycradit'] = userinfo['cradit']
                    userinfo['debt'].clear()
                else:
                    date = time.strftime("%Y-%m-%d")
                    dic = {"date": date,
                           "money": sum_money,
                           "info": "上个月欠款"
                           }
                    userinfo['kycradit'] = userinfo['cradit']
                    userinfo['debt'].clear()
                    userinfo['debt'].append(dic)
                json.dump(userinfo, open(os.path.join(setting.USER_DIR_FOLDER, cardnum, 'basic_info.json'), 'w'))



def run():
    mian()
