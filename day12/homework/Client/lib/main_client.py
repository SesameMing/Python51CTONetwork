#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-05 19:37
# Version：3.x
import os
import json
import time
import logging
import pymysql
from config import setting

DB_DICT = {}  # Database config dict

def setloggin():
    """
    set a log
    :return: log object
    """
    logger = logging.getLogger('客户端')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s %(levelname)s] %(message)s'))
    logger.addHandler(ch)
    return logger

Log = setloggin()


def db():
    """

    :return:
    """
    Log.info("检查配置")
    if os.path.exists(setting.BD_FILE_PATH):
        DB_DICT = json.load(open(setting.BD_FILE_PATH, 'r'))
        if DB_DICT.get('db_host') and DB_DICT.get('db_name'):
            pass
        else:
            pass
    else:
        Log.info("第一次登录，请先配置数据库")
        time.sleep(.1)
        while True:
            db_host = input("数据库地址：").strip()
            db_port = input("数据库端口：").strip()
            db_username = input("数据库用户名：").strip()
            db_password = input("数据库密码：").strip()
            db_name = input("数据库名称：").strip()
            try:
                Log.info("正在尝试链接数据库.")
                DB_DICT = {"db_host": db_host, "db_port": db_port, "db_username": db_username,
                           "db_password": db_password, "db_name": db_name}
                db_conn = pymysql.connect(db_host, db_username, db_password, db_name, int(db_port))
                json.dump(DB_DICT, open(setting.BD_FILE_PATH, 'w'))

                return True
            except Exception as e:
                print(e)
                Log.warning("数据库链接失败，请重试。")
                time.sleep(.1)


def run():
    Log.info("启动程序")
    if db():
        print(setting.BASE_PATH)
        print('run')
        print(DB_DICT)
