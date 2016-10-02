#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-01 15:38
import sys
import time
from modules.lib import Gaofushuai, Diaosi, Meinv


def run():
    John = Diaosi.Diaosi('John', '男', '18', '学生', '黄种人', '中国', '编程运维', 1000, 0, 0)
    Liz = Meinv.Meinv('Liz', '女', '18', '学生', '黄种人', '中国', '逛街，购物', 1000, 0, 0)
    Peter = Gaofushuai.Gaofushuai('Peter', '男', '18', '富二代', '黄种人', '中国', '泡妞', 2000000, 0, 0)