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
from bin.lib import mysql_table
USER_LOGIN_STATUS = {'username': None, 'login': False}
DB_DICT = {}  # Database config dict
QUIT_CHAR = 'q'

#  一些设置
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


# 程序主要部分
def setHost():
    while True:
        mun = """-------------------------------------
|              主机列表             |
-------------------------------------"""
        print(mun)
        ret = sqlobj.showHost()
        if len(ret) == 0:
            mun = """|         暂无主机,请先添加         | """
            print(mun)
        else:
            hostlist = []  # 主机列表
            for item in ret:
                hostlist.append(item)
                print(item.id, item.nickname, item.ip)

        mun = """-------------------------------------
| a:添加 e:编辑 d:删除 %s:返回主菜单 |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        innp = input("请输入你的选择>>>:")
        if innp == "a":
            hostname = input("[为空则取消]输入新添加的主机名称>>>:").strip()
            if not hostname:
                Log.info("取消操作")
                time.sleep(.1)
                continue
            hostip = input("[为空则取消]输入新添加的ip地址>>>:").strip()
            if not hostip:
                Log.info("取消操作")
                time.sleep(.1)
                continue
            ret = sqlobj.showHostfz()
            while True:
                if len(ret) == 0:
                    Log.warning("暂无分组，请先添加分组")
                    classname = input("[为空则取消]请先添加分组>>>:").strip()
                    if not classname:
                        Log.info("取消操作")
                        time.sleep(.1)
                        continue
                    else:
                        ret = sqlobj.setHostfz(classname)
                        if ret:
                            Log.info("添加成功")
                        else:
                            Log.info("添加失败")
                        time.sleep(.1)
                else:
                    clidlist = []
                    for item in ret:
                        clidlist.append(item.id)
                        print(item.id, item.classname)
                    cid = input("[为空则取消]请选择主机分组>>>:").strip()
                    if not cid:
                        Log.info("取消操作")
                        time.sleep(.1)
                        break
                    else:
                        if int(cid) in clidlist:
                            pass
                        else:
                            Log.info("")
                            time.sleep(.1)
                            break


        else:
            pass


def setHostfz():
    """
    设置 host 分组
    :return:
    """
    while True:
        mun = """-------------------------------------
|              分组列表             |
-------------------------------------"""
        print(mun)
        ret = sqlobj.showHostfz()
        if len(ret) == 0:
            mun = """|         暂无分组,请先添加         | """
            print(mun)
        else:
            clidlist = []  # 分类id列表
            for item in ret:
                clidlist.append(item.id)
                print(item.id, '.  ', item.classname)
        mun = """-------------------------------------
| a:添加 e:编辑 d:删除 %s:返回主菜单 |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        innp = input("请输入你的选择>>>:")
        if innp == "a":
            hostinnp = input("[为空则取消]输入新添加的分类名称>>>:").strip()
            if not hostinnp:
                Log.info("取消添加")
                time.sleep(.1)
                continue
            else:
                ret = sqlobj.setHostfz(hostinnp)
                if ret:
                    Log.info("添加成功")
                else:
                    Log.info("添加失败")
                time.sleep(.1)
                continue
        elif innp == "e":
            hostinnpid = input("[为空则取消]请输入要修改分类的id>>>:").strip()
            if not hostinnpid:
                Log.info("取消修改")
                time.sleep(.1)
                continue
            else:
                if hostinnpid.isdigit():
                    if int(hostinnpid) in clidlist:
                        classname = input("[为空则取消]请输入新的分组名称>>>:").strip()
                        if not classname:
                            Log.info("取消修改")
                            time.sleep(.1)
                            continue
                        else:
                            if sqlobj.editHostfz(hostinnpid, classname):
                                Log.info("修改成功")
                                time.sleep(.1)
                                continue
                            else:
                                Log.warning("修改失败")
                                time.sleep(.1)
                                continue
                    else:
                        Log.warning("输入错误,不在范围内")
                        time.sleep(.1)
                        continue
                else:
                    Log.warning("输入错误")
                    time.sleep(.1)
                    continue
        elif innp == "d":
            hostinnpid = input("[为空则取消]请输入要删除分类的id>>>:").strip()
            if not hostinnpid:
                Log.info("取消删除")
                time.sleep(.1)
                continue
            else:
                if hostinnpid.isdigit():
                    if int(hostinnpid) in clidlist:
                        qr = input("[y:删除/n:取消”]是否确定删除：>>>:").strip()
                        if qr == 'y':
                            if sqlobj.delHostfz(hostinnpid):
                                Log.info("删除成功")
                                time.sleep(.1)
                                continue
                            else:
                                Log.warning("删除失败")
                                time.sleep(.1)
                                continue
                        else:
                            Log.info("取消删除")
                            time.sleep(.1)
                            continue
                    else:
                        Log.warning("输入错误,不在范围内")
                        time.sleep(.1)
                        continue
                else:
                    Log.warning("输入错误")
                    time.sleep(.1)
                    continue
        elif innp == QUIT_CHAR:
            Log.info("返回主菜单")
            time.sleep(.1)
            break
        else:
            Log.warning("错误的选项输入")
            time.sleep(.1)
            continue


def setRabbitmq():
    """
    配置Rabbitmq
    :return:
    """
    if not os.path.exists(setting.RB_FILE_PATH):
        rbhost = input("请先配置RabbitMQ服务器地址：").strip()
        while not rbhost:
            rbhost = input("RabbitMQ服务器地址不能为空，请重新配置：").strip()
        dic = {"rbhost": rbhost}
        json.dump(dic, open(setting.RB_FILE_PATH, 'w'))
        Log.info("设置")
    while True:
        rbhost_dic = json.load(open(setting.RB_FILE_PATH, 'r'))
        mun = """-------------------------------------
| RabbitMQ服务器地址: %s
-------------------------------------
| e:修改        %s:返回上级
-------------------------------------""" % (rbhost_dic['rbhost'], QUIT_CHAR)
        print(mun)
        innp = input("请输入你的选择>>>:").strip()
        if innp == 'e':
            host_innp = input("[为空则取消修改]请输入你新的RabbitMQ>>>:").strip()
            if not host_innp:
                Log.info("取消修改")
                time.sleep(.1)
                continue
            else:
                rbhost_dic['rbhost'] = host_innp
                json.dump(rbhost_dic, open(setting.RB_FILE_PATH, 'w'))
                Log.info("修改成功")
                time.sleep(.1)
                continue
        elif innp == QUIT_CHAR:
            Log.info("返回主菜单")
            time.sleep(.1)
            break
        else:
            Log.warning("错误的选项输入")
            time.sleep(.1)
            continue


def main():
    """
    主方法
    :return:
    """
    while True:
        mun = """-------------------------------------
|     简单远程调用模型PRC v1.0.0    |
-------------------------------------
|                                   |
|  1.设置RabbitMQ服务器链接         |
|  2.主机分组                       |
|  3.主机列表                       |
|  4.下发任务                       |
|                                   |
-------------------------------------
| 数字：选择            %s:退出      |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        inpp = input("请输入你的选择>>>:").strip()
        if inpp == QUIT_CHAR:
            break
        elif inpp.isdigit():
            if int(inpp) == 1:
                setRabbitmq()
            elif int(inpp) == 2:
                setHostfz()
            elif int(inpp) == 3:
                setHost()
            elif int(inpp) == 4:
                pass
            else:
                pass
        else:
            pass


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
        sqlobj = mysqlobj()
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
                    sqlobj = mysqlobj()
                    obj = sqlobj.init()
                    user = input("设置管理员帐号：").strip()
                    while user is null:
                        user = input("管理员帐号不能为空,重新设置：").strip()
                    passwd = input("设置管理员密码：").strip()
                    while passwd is null:
                        passwd = input("管理员密码不能为空,重新设置：").strip()
                    sqlobj.setadmin(user, passwd)
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
        global sqlobj
        sqlobj = mysqlobj()
        main()


