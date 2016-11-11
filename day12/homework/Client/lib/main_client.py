#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-05 19:37
# Version：3.x
import os
import sys
import json
import time
import logging
import pymysql
from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database
from config import setting
from lib.mysql import mysql_table
USER_LOGIN_STATUS = {'username': None, 'login': False}
DB_DICT = {}  # Database config dict
QUIT_CHAR = 'q'


def setloggin():
    """
    设置log
    :return: log对象
    """
    logger = logging.getLogger('客户端')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s %(levelname)s] %(message)s'))
    logger.addHandler(ch)
    return logger

Log = setloggin()


def mysqlobj():
    """
    实例化 sqlalchemy对象
    :return: sqlalchemy对象
    """
    conn = mysql_table.initdatebase()
    return conn

sqlobj = mysqlobj()


def main():
    str1 = """---------主菜单-----------

1.设置RabbitMQ服务器链接
2.主机分组
3.主机列表
4.下发任务

--------------------------
"""
    print(str1)

def login():
    """
    用户登录方法
    :return: bool
    """
    Log.info("用户登录")
    time.sleep(.1)
    while True:
        username = input("请输入帐号：").strip()
        while not username:
            username = input("帐号不能把为空,请重新输入：").strip()
        password = input("请输入密码：").strip()
        while not password:
            password = input("密码不能把为空,请重新输入：").strip()
        if sqlobj.yzuser(username, password):
            Log.info("登录成功")
            USER_LOGIN_STATUS['username'] = username
            USER_LOGIN_STATUS['login'] = True
            time.sleep(.1)
            return True
        else:
            Log.warning("帐号密码错误,请重新输入")
            time.sleep(.1)


def ini_db():
    """
    检查数据
    :return: bool
    """
    Log.info("检查配置")
    if os.path.exists(setting.BD_FILE_PATH):
        DB_DICT = json.load(open(setting.BD_FILE_PATH, 'r'))
        if DB_DICT.get('db_host') and DB_DICT.get('db_name'):
            dbstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (DB_DICT['db_username'], DB_DICT['db_password'], DB_DICT['db_host'], DB_DICT['db_port'], DB_DICT['db_name'])

        else:
            pass
        return True
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
                dbstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (db_username, db_password, db_host, db_port, db_name)
                engine = create_engine(dbstr, echo=True, max_overflow=5)
                if not database_exists(engine.url):
                    Log.info("数据库不存在，新建数据库【%s】" % db_name)
                    create_database(engine.url)
                    json.dump(DB_DICT, open(setting.BD_FILE_PATH, 'w'))
                    time.sleep(.1)
                    obj = sqlobj.init()
                    user = input("设置管理员帐号：").strip()
                    while user is null:
                        user = input("管理员帐号不能为空,重新设置：").strip()
                    passwd = input("设置管理员密码：").strip()
                    while passwd is null:
                        passwd = input("管理员密码不能为空,重新设置：").strip()
                    obj.setadmin(user, passwd)
                return True
            except Exception as e:
                print(e)
                Log.warning("数据库链接失败，请重试。")
                time.sleep(.1)



def run():
    Log.info("启动程序")
    if not ini_db():
        Log.info("数据库配置异常，请先删除config/db.conf文件")
        sys.exit(1)
    if login():
        main()


