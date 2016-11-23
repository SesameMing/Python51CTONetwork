#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-22 15:46
# Version：3.x
import os
import logging
import time
import json
from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database
from bin.lib import setting, mysql_table


def setloggin():
    """
    设置log
    :return: log对象
    """
    logger = logging.getLogger('服务端')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s %(levelname)s] %(message)s'))
    logger.addHandler(ch)
    return logger

Log = setloggin()  # 获取Loggin对象


def mysqlobj():
    """
    实例化 sqlalchemy对象
    :return: sqlalchemy对象
    """
    conn = mysql_table.database()
    return conn




def check_db():
    """
    检查数据库配置文件
    :return: bool
    """
    if os.path.exists(setting.BD_FILE_PATH):  # 检查数据库文件是否存在 存在： 就检查能否链接上数据库 不存在：创建数据库链接文件
        pass

    else:
        Log.info("第一次登录，请先配置数据库")
        time.sleep(.1)
        db_host = input("数据库地址：").strip()
        db_port = input("数据库端口：").strip()
        db_username = input("数据库用户：").strip()
        db_password = input("数据库密码：").strip()
        db_dbname = input("数据库名称：").strip()

        DB_DICT = {"db_host": db_host, "db_port": db_port, "db_username": db_username,
                   "db_password": db_password, "db_dbname": db_dbname}
        dbstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (db_username, db_password, db_host, db_port, db_dbname)
        engine = create_engine(dbstr, echo=True, max_overflow=5)
        if not database_exists(engine.url):  # 判断设置的数据库信息是否存在，不存在就新建数据库
            Log.info("数据库不存在，新建数据库【%s】" % db_dbname)
            create_database(engine.url)
            json.dump(DB_DICT, open(setting.BD_FILE_PATH, 'w'))  # 将数据库配置写入配置文件
            time.sleep(.1)
            objsql = mysqlobj()
            objsql.create_table()


        else:
            pass


def run():
    """
    程序入口
    :return:
    """
    Log.info("启动程序")
    time.sleep(.1)  # 延时0.1秒 防止 log输出 和 程序输出的顺序变化
    if not check_db():
        Log.warning("数据检查异常")
        exit(1)

