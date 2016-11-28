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
USER_LOGIN_STATUS = {"username": None, "login": False, "admin": False}  # 登录状态记录
QUIT_CHAR = 'q'

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


def UserClass():
    """
    用户分类
    :return:
    """
    while True:
        mun = """-------------------------------------
|            用户分组列表           |
-------------------------------------"""
        print(mun)
        ret = objsql.queryAllUserClass()
        grouplist = []
        if len(ret) == 0:
            mun = """|         暂无分组,请先添加         | """
            print(mun)
        else:
            for item in ret:
                grouplist.append(item)
                print(item.id, item.title)
        mun = """-------------------------------------
| a:添加 e:编辑 d:删除 %s:返回主菜单 |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        innp = input("请输入你的选择>>>:")




def HostList():
    """
    主机列表
    :return:
    """
    while True:
        mun = """-------------------------------------
|              主机列表             |
-------------------------------------"""
        print(mun)
        ret = objsql.queryAllHostList()
        hostlist = []  # 主机列表
        if len(ret) == 0:
            mun = """|         暂无主机,请先添加         | """
            print(mun)
        else:
            for item in ret:
                hostlist.append(item)
                print(item.id, item.ip_name, item.ip_host)

        mun = """-------------------------------------
| a:添加 e:编辑 d:删除 %s:返回主菜单 |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        innp = input("请输入你的选择>>>:")
        if innp == "a":  # 添加主机
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
            while True:
                ret = objsql.queryAllHostClass()
                if len(ret) == 0:
                    # 没有分组分组，先添加分组
                    Log.warning("暂无分组，请先添加分组")
                    time.sleep(.1)
                    classname = input("[为空则取消]请先添加分组>>>:").strip()
                    if not classname:
                        Log.info("取消操作")
                        time.sleep(.1)
                        continue
                    else:
                        ret = objsql.addHostClass(classname)
                        if ret:
                            Log.info("添加成功")
                        else:
                            Log.info("添加失败")
                        time.sleep(.1)
                else:
                    # 有分组，添加主机列表
                    clidlist = []
                    for item in ret:
                        clidlist.append(item.id)
                        print(item.id, item.title)
                    cid = input("[为空则取消]请选择主机分组id>>>:").strip()
                    if not cid:
                        Log.info("取消操作")
                        time.sleep(.1)
                        break
                    else:
                        if int(cid) in clidlist:
                            if objsql.addHost(hostname, cid, hostip):
                                Log.info("添加成功")
                                time.sleep(.1)
                                break
                            else:
                                Log.warning("添加失败")
                                time.sleep(.1)
                                break
                        else:
                            Log.info("选择主机分组错误")
                            time.sleep(.1)
                            continue
        elif innp == "e":
            # 编辑主机
            if len(hostlist) == 0:
                Log.info("主机都是空的,修改什么呢")
                time.sleep(.1)
                continue
            edithostid = input("[为空则取消]输入需要修改的主机id>>>:").strip()
            if edithostid.isdigit():
                # 判断用户输入是不是数字
                if int(edithostid) in [i.id for i in hostlist]:
                    newhostname = input("[为空则不修改]输入需要新的主机昵称>>>:").strip()
                    if not newhostname:
                        newhostname = False
                    newhostip = input("[为空则不修改]输入需要新的主机ip>>>:").strip()
                    if not newhostip:
                        newhostip = False
                    if newhostname is False and newhostip is False:
                        # 没有更新信息
                        Log.info("没有修改主机")
                        time.sleep(.1)
                        continue
                    else:
                        # 更新信息
                        if objsql.editHost(edithostid, newhostname, newhostip):
                            Log.info("修改成功")
                            time.sleep(.1)
                            continue
                        else:
                            Log.warning("修改失败")
                            time.sleep(.1)
                            continue
                else:
                    # 用户输入不在主机列表范围内
                    Log.warning("输入不在范围内")
                    time.sleep(.1)
                    continue
            else:
                # 用户选择主机不是输入的数字
                Log.warning("输入错误")
                time.sleep(.1)
                continue

        elif innp == "d":
            # 删除主机
            if len(hostlist) == 0:
                Log.info("主机都是空的,删除什么呢")
                time.sleep(.1)
                continue
            hostid = input("[为空则取消]请输入要删除的主机id>>>:").strip()
            if not hostid:
                Log.info("取消删除")
                time.sleep(.1)
                continue
            else:
                if int(hostid) in [i.id for i in hostlist]:
                    qr = input("[y:删除/n:取消”]是否确定删除：>>>:").strip()
                    if qr == 'y':
                        if objsql.delHost(hostid):
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
                    Log.warning("输入不在范围内")
                    time.sleep(.1)
                    continue

        elif innp == QUIT_CHAR:
            Log.info("返回主菜单")
            time.sleep(.1)
            break
        else:
            Log.warning("输入错误。请重新输入")
            time.sleep(.1)
            continue


def HostClass():
    """
    管理主机分类
    :return:
    """
    while True:
        msg = """-------------------------------------
|              分组列表             |
-------------------------------------"""
        print(msg)
        ret = objsql.queryAllHostClass()
        clidlist = []  # 分类id列表
        if len(ret) == 0:
            mun = """|         暂无分组,请先添加         | """
            print(mun)
        else:
            for item in ret:
                clidlist.append(item.id)
                print(item.id, '.  ', item.title)
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
                ret = objsql.addHostClass(hostinnp)
                if ret:
                    Log.info("添加成功")
                else:
                    Log.info("添加失败")
                time.sleep(.1)
                continue
        elif innp == "e":  # 编辑分组 修改名称
            if len(clidlist) == 0:  # 分组长度为空
                Log.info("分组都是空的,修改什么呢")
                time.sleep(.1)
                continue
            hostinnpid = input("[为空则取消]请输入要修改分类的id>>>:").strip()
            if not hostinnpid:
                Log.info("取消修改")
                time.sleep(.1)
                continue
            else:
                if hostinnpid.isdigit():  # 判断输入的字符为数字
                    if int(hostinnpid) in clidlist:
                        classname = input("[为空则取消]请输入新的分组名称>>>:").strip()
                        if not classname:
                            Log.info("取消修改")
                            time.sleep(.1)
                            continue
                        else:
                            if objsql.editHostClass(hostinnpid, classname):  # 执行更新数据库操作
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
        elif innp == "d":  # 执行删除
            if len(clidlist) == 0:
                Log.info("分组都是空的,删除什么呢")
                time.sleep(.1)
                continue
            hostinnpid = input("[为空则取消]请输入要删除分类的id>>>:").strip()
            if not hostinnpid:
                Log.info("取消删除")
                time.sleep(.1)
                continue
            else:
                if hostinnpid.isdigit():
                    if int(hostinnpid) in clidlist:
                        qr = input("[y:删除/n:取消”]是否确定删除：>>>:").strip()
                        if qr == 'y':  # 二次确认删除
                            if objsql.delHostClass(hostinnpid):  # 执行删除数据库操作
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
                        # 输入的删除id不在分类中
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


def setrbmq():
    """
    设置rabbitmq服务器
    :return:
    """
    if not os.path.exists(setting.RB_FILE_PATH):  # rabbitmq配置文件不存在
        rbhost = input("请先配置RabbitMQ服务器地址：").strip()
        while not rbhost:
            rbhost = input("RabbitMQ服务器地址不能为空，请重新配置：").strip()
        dic = {"rbhost": rbhost}
        json.dump(dic, open(setting.RB_FILE_PATH, 'w'))  # 将rabbitmq服务器地址写入配置文件
        Log.info("设置")
        time.sleep(.1)
    while True:
        rbhost_dic = json.load(open(setting.RB_FILE_PATH, 'r'))  # 读取rabbitmq配置文件
        mun = """-------------------------------------
| RabbitMQ服务器地址: %s
-------------------------------------
| e:修改        %s:返回上级
-------------------------------------""" % (rbhost_dic['rbhost'], QUIT_CHAR)
        print(mun)
        innp = input("请输入你的选择>>>:").strip()
        if innp == 'e':  # 编辑rabbitmq配置文件
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
    程序主程序
    :return:
    """
    while True:
        if USER_LOGIN_STATUS['admin']:
            # 登录用户是管理员 显示管理员菜单
            print("管理员界面")
            msg = """
1.设置RabbitMQ服务器
2.主机分组
3.主机列表
4.用户分组
5.用户列表
"""
            print(msg)
            inpp = input("请输入选择序号>>>：")
            if inpp == QUIT_CHAR:
                break
            else:
                if inpp == '1':
                    # 设置RabbitMQ服务器
                    setrbmq()
                elif inpp == '2':
                    # 主机分组
                    HostClass()
                elif inpp == '3':
                    # 主机列表
                    HostList()
                elif inpp == '4':
                    UserClass()


        else:
            print("普通用户登录界面")


def login():
    """
    用户登录 1.管理员登录 2.用户成员登录
    :return:bool
    """
    pring_msg = """-----------------------
1. 管理员登录
2. 用户登录
-----------------------"""
    print(pring_msg)
    while True:
        logintype = input("[%s:退出]请选择登录类型>>>:" % QUIT_CHAR).strip()
        if logintype == QUIT_CHAR:
            # 退出
            break
        elif logintype == '1':
            # 管理员登录
            username = input("管理员帐号：").strip()
            while not username:
                username = input("管理员帐号不能为空：").strip()
            password = input("管理员密码：").strip()
            while not password:
                password = input("管理员密码不能为空：").strip()
            ret = objsql.queryAdmin(username, password)
            if ret:
                USER_LOGIN_STATUS['username'] = username
                USER_LOGIN_STATUS['login'] = True
                USER_LOGIN_STATUS['admin'] = True
                return True
            else:
                Log.warning("帐号密码错误")
                time.sleep(.1)
        elif logintype == '2':
            # 用户登录
            pass
        else:
            # 错误输入
            pass


def check_db():
    """
    检查数据库配置文件
    :return: bool
    """
    if os.path.exists(setting.BD_FILE_PATH):  # 检查数据库文件是否存在 存在： 就检查能否链接上数据库 不存在：创建数据库链接文件
        return True

    else:
        Log.info("第一次登录，请先配置数据库")
        time.sleep(.1)
        db_host = input("数据库地址：").strip()
        db_port = input("数据库端口：").strip()
        db_username = input("数据库用户：").strip()
        db_password = input("数据库密码：").strip()
        db_dbname = input("数据库名称：").strip()

        try:
            DB_DICT = {"db_host": db_host, "db_port": db_port, "db_username": db_username,
                       "db_password": db_password, "db_dbname": db_dbname}
            dbstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (db_username, db_password, db_host, db_port, db_dbname)
            engine = create_engine(dbstr, echo=True, max_overflow=5)
            if not database_exists(engine.url):  # 判断设置的数据库信息是否存在，不存在就新建数据库
                Log.info("数据库不存在，新建数据库【%s】" % db_dbname)
                create_database(engine.url)
                json.dump(DB_DICT, open(setting.BD_FILE_PATH, 'w'))  # 将数据库配置写入配置文件
                time.sleep(.1)

                objsql = mysqlobj()  # 实例化sqlalchemy
                objsql.create_table()  # 创建数据库

                user = input("设置管理员帐号：").strip()
                while user is null:
                    user = input("管理员帐号不能为空,重新设置：").strip()
                passwd = input("设置管理员密码：").strip()
                while passwd is null:
                    passwd = input("管理员密码不能为空,重新设置：").strip()
                objsql.setAdminUser(user, passwd)
            else:
                json.dump(DB_DICT, open(setting.BD_FILE_PATH, 'w'))
            return True
        except Exception as e:
            print(e)
            Log.warning("数据库链接失败，请重试。")
            time.sleep(.1)


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
    global objsql
    objsql = mysqlobj()
    if login():
        main()

