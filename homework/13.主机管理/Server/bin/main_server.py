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
from bin.lib import setting, mysql_table, rabbit_mq
USER_LOGIN_STATUS = {"username": None, "login": False, "admin": False, "uid": None}  # 登录状态记录
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


def rbmqobj():
    obj = rabbit_mq.rabbit()
    return obj


def run_common():
    while True:
        innp = input("[%s退出]需要发送的命令>>>:" % QUIT_CHAR).strip()
        while not innp:
            innp = input("[%s退出]命令不能为空,需要发送的命令>>>:" % QUIT_CHAR).strip()
        if innp == QUIT_CHAR:
            Log.info("退出发送指令")
            time.sleep(.1)
            break
        else:
            while True:
                mun = """-------------------------------------
|              发送类型             |
-------------------------------------
|                                   |
|  1.全部发送                       |
|  2.主机单独发送                   |
|                                   |
-------------------------------------"""
                print(mun)
                sendtype = input("[%s退出]选择发送的类型>>>:" % QUIT_CHAR).strip()
                while not sendtype:
                    sendtype = input("[%s退出]类型不能为空,请重新输入>>>:" % QUIT_CHAR).strip()
                if sendtype == QUIT_CHAR:
                    Log.info("退出发送指令")
                    time.sleep(.1)
                    break
                elif sendtype == '1':
                    Hostlist = objsql.showUserHost(USER_LOGIN_STATUS['uid'])
                    hostip = []
                    for item in Hostlist:
                        hostip.append(item.ip_host)
                    print("发送给了 %s 个主机" % len(hostip))
                    rb = rbmqobj()
                    rb.sendmsg(innp, hostip)
                    rb.remsg("serverquer", hostip)
                    break
                elif sendtype == '2':
                    Hostlist = objsql.showUserHost(USER_LOGIN_STATUS['uid'])

                    if len(Hostlist) == 0:
                        mun = """|         暂无主机,请先添加分组         | """
                        print(mun)
                        Log.warning("还不存在主机，请先添加分组")
                        time.sleep(.1)
                        break
                    else:
                        for item in Hostlist:
                            print(item.id, '.  ', item.ip_name, item.ip_host)
                        hostid = input("[%s退出]请选择主机id>>>:" % QUIT_CHAR).strip()
                        while not hostid:
                            hostid = input("[%s退出]主机id不能为空,请选择分组>>>:" % QUIT_CHAR).strip()
                        if hostid == QUIT_CHAR:
                            Log.info("退出")
                            time.sleep(.1)
                            break
                        elif hostid.isdigit():
                            if int(hostid) in [i.id for i in Hostlist]:
                                jshost = objsql.gethost(hostid)
                                rb = rbmqobj()
                                rb.sendmsg(innp, jshost)
                                rb.remsg("serverquer", jshost)
                            else:
                                Log.warning("错误的主机选择,重新选择")
                                time.sleep(.1)
                                continue
                        else:
                            Log.warning("错误的主机选择,重新选择")
                            time.sleep(.1)
                            continue

def showHostlist():
    while True:
        mun = """-------------------------------------
|              主机列表             |
-------------------------------------"""
        print(mun)
        ret = objsql.showUserHost(USER_LOGIN_STATUS['uid'])
        hostlist = []  # 主机列表
        if len(ret) == 0:
            mun = """|         暂无主机,请先添加         | """
            print(mun)
        else:
            for item in ret:
                hostlist.append(item)
                print(item.id, item.ip_name, item.ip_host)

        mun = """-------------------------------------
| %s:返回主菜单                       |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        innp = input("请输入你的选择>>>:")
        if innp == QUIT_CHAR:
            break
        else:
            continue


def UserList():
    """
    用户列表
    :return:
    """
    while True:
        mun = """-------------------------------------
|              用户列表             |
-------------------------------------"""
        print(mun)
        ret = objsql.queryAllUser()
        userlist = []  # 主机列表
        if len(ret) == 0:
            mun = """|         暂无用户,请先添加         | """
            print(mun)
        else:
            for item in ret:
                userlist.append(item.User.id)
                print(item.User.id, item.Group.title, item.User.username)

        mun = """-------------------------------------
| a:添加 e:编辑 d:删除 %s:返回主菜单 |
-------------------------------------""" % QUIT_CHAR
        print(mun)
        innp = input("请输入你的选择>>>:")
        if innp == 'a':  # 添加用户
            username = input("[为空则取消]输入新添加的用户名称>>>:").strip()
            if not username:
                Log.info("取消操作")
                time.sleep(.1)
                continue
            password = input("[为空则取消]输入新添加的用户密码>>>:").strip()
            if not password:
                Log.info("取消操作")
                time.sleep(.1)
                continue

            ret = objsql.queryAllUserGroup()
            if len(ret) == 0:
                # 没有分组分组，先添加分组
                Log.warning("暂无分组，请先添加分组")
                time.sleep(.1)
                continue
            else:
                grouplist = []
                for item in ret:
                    grouplist.append(item.id)
                    print(item.id, item.title)
                usergroup = input("[为空则取消]请选择用户分组id>>>:").strip()

                if not usergroup:
                    Log.info("取消操作")
                    time.sleep(.1)
                    continue
                else:
                    if int(usergroup) not in grouplist:
                        Log.warning("选择的用户组不存在")
                        time.sleep(.1)
                        continue
                    else:
                        if objsql.addUser(username, password, usergroup):
                            Log.info("添加用户成功")
                            time.sleep(.1)
                            continue
                        else:
                            Log.warning("添加用户失败")
                            time.sleep(.1)
                            continue
        elif innp == 'e':
            # 编辑用户信息
            if len(userlist) == 0:
                Log.warning("用户列表为空，修改什么呢").strip()
                time.sleep(.1)
                continue
            else:
                userid = input("[为空则取消]请输入需要修改的用户id：").strip()
                if not userid:
                    Log.info("取消修改")
                    time.sleep(.1)
                    continue
                else:
                    if userid.isdigit():
                        # 用户输入的用户id为数字
                        if int(userid) in userlist:
                            # 用户输入的id在范围内
                            password = input("[为空则不修改该项]请输入需要新的密码：").strip()
                            if not password:
                                password = False
                            gid = input("[为空则不修改该项]请输入需要用户分组：").strip()
                            if not gid:
                                gid = False
                            if password is False and gid is False:
                                # 修改项都为Fasle 则不修改
                                Log.info("没有做任何修改")
                                time.sleep(.1)
                                continue
                            else:
                                # 修改用户信息
                                if objsql.editUser(userid, password, gid):
                                    Log.info("修改成功")
                                    time.sleep(.1)
                                    continue
                                else:
                                    Log.warning("修改失败")
                                    time.sleep(.1)
                                    continue
                        else:
                            # 用户输入的id不在范围内
                            Log.warning("错误的用户id")
                            time.sleep(.1)
                            continue
                    else:
                        # 用户输入的id不为数字
                        Log.warning("错误的输入")
                        time.sleep(.1)
                        continue

        elif innp == 'd':
            if len(grouplist) == 0:
                Log.warning("都没有用户删除什么呢")
                time.sleep(.1)
                continue
            else:
                userid = input("[为空则取消]请输入需要删除的用户id：")
                if not userid:
                    Log.info("取消删除")
                    time.sleep(.1)
                    continue
                else:
                    if userid.isdigit():
                        if int(userid) in [i.id for i in grouplist]:
                            qr = input("[y:删除/n:取消”]是否确定删除：>>>:").strip()
                            if qr == 'y':  # 二次确认删除
                                if objsql.delUserGroup(userid):  # 执行删除数据库操作
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
            # 返回上级
            Log.info("返回主菜单")
            time.sleep(.1)
            break
        else:
            # 错误的选择
            Log.warning("错误的选择")
            time.sleep(.1)
            continue


def UserGroup():
    """
    用户分类
    :return:
    """
    while True:
        mun = """-------------------------------------
|            用户分组列表           |
-------------------------------------"""
        print(mun)
        ret = objsql.queryAllUserGroup()  # 数据库查询用户分组列表
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
        innp = input("请输入你的选择>>>:").strip()
        if innp == 'a':
            # 添加用户分组
            groupname = input("[为空则取消]输入新添加的用户分组名称>>>:").strip()
            if not groupname:
                Log.info("取消操作")
                time.sleep(.1)
                continue
            hostclass = objsql.queryAllHostClass()  # 查询所有的主机分组
            clidlist = [0, ]  # 分类id列表
            if not hostclass:
                mun = """  暂时没有主机分组 """
                print(mun)
            else:
                for hc in hostclass:
                    clidlist.append(hc.id)
                    print(hc.id, '. ', hc.title)
            c_id = input("请输入分组分配主机分组id：").strip()
            while int(c_id) not in clidlist:
                # 选择的分组不存在
                c_id = input("不存在的分组id：")

            if objsql.addUserGroup(groupname, c_id):
                Log.info("添加成功")
                time.sleep(.1)
                continue
            else:
                Log.warning("添加失败")
                time.sleep(.1)
                continue
        elif innp == 'e':
            # 修改用户分组
            if len(grouplist) == 0:
                Log.warning("都没有分组修改什么呢")
                time.sleep(.1)
                continue
            else:
                groupid = input("[为空则取消]请输入需要修改的分组id：")
                if not groupid:
                    Log.info("取消修改")
                    time.sleep(.1)
                    continue
                else:
                    if groupid.isdigit():
                        # 判断用户输入的数字
                        print(grouplist)
                        if int(groupid) in [i.id for i in grouplist]:
                            # 输入的id号在范围内
                            new_group_name = input("[为空则取消]请输入新的分组名称：").strip()
                            if not new_group_name:
                                new_group_name = False
                            new_host_class_id = input("[为空则不修改]输入主机分组id>>>:").strip()
                            if not new_host_class_id:
                                new_host_class_id = False
                            if new_group_name is False and new_host_class_id is False:
                                # 没有更新信息
                                Log.info("没有修改主机")
                                time.sleep(.1)
                                continue
                            else:
                                if objsql.editUserGroup(groupid, new_group_name, new_host_class_id):
                                    Log.info("修改成功")
                                    time.sleep(.1)
                                    continue
                                else:
                                    Log.warning("修改失败")
                                    time.sleep(.1)
                                    continue
                        else:
                            # 用户输入的分组id不是不在范围内
                            Log.warning("分组id不在范围内")
                            time.sleep(.1)
                            continue
                    else:
                        # 用户输入的分组id不是数字类型
                        Log.warning("分组id不是数字类型")
                        time.sleep(.1)
                        continue
        elif innp == 'd':
            # 删除用户分组
            if len(grouplist) == 0:
                Log.warning("都没有分组删除什么呢")
                time.sleep(.1)
                continue
            else:
                groupid = input("[为空则取消]请输入需要删除的分组id：")
                if not groupid:
                    Log.info("取消删除")
                    time.sleep(.1)
                    continue
                else:
                    if groupid.isdigit():
                        if int(groupid) in [i.id for i in grouplist]:
                            qr = input("[y:删除/n:取消”]是否确定删除：>>>:").strip()
                            if qr == 'y':  # 二次确认删除
                                if objsql.delUserGroup(groupid):  # 执行删除数据库操作
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
            # 返回上级
            Log.info("返回主菜单")
            time.sleep(.1)
            break
        else:
            # 错误的选择
            continue


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
            mun = """-------------------------------------
|             管理员界面            |
-------------------------------------
|                                   |
|  1.设置RabbitMQ服务器链接         |
|  2.主机分组                       |
|  3.主机列表                       |
|  4.用户分组                       |
|  5.用户列表                       |
|                                   |
-------------------------------------
|    数字：选择         %s:退出      |
-------------------------------------""" % QUIT_CHAR
            print(mun)
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
                    UserGroup()
                elif inpp == '5':
                    UserList()
        else:
            mun = """-------------------------------------
|             普通用户              |
-------------------------------------
|                                   |
|  1.查看所有主机                   |
|  2.下发任务                       |
|                                   |
-------------------------------------
|    数字：选择         %s:退出      |
-------------------------------------""" % QUIT_CHAR
            print(mun)
            innp = input("请输入选择序号>>>：")
            if innp == QUIT_CHAR:
                break
            else:
                if innp == '1':
                    showHostlist()
                elif innp == '2':
                    run_common()
                else:
                    pass



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
            username = input("登录帐号：")
            while not username:
                username = input("登录帐号不能为空：")

            password = input("密码：")
            while not password:
                password = input("登录密码不能为空")
            ret = objsql.queryUser(username, password)
            if ret:
                USER_LOGIN_STATUS['username'] = username
                USER_LOGIN_STATUS['login'] = True
                USER_LOGIN_STATUS['admin'] = False
                USER_LOGIN_STATUS['uid'] = ret
                return True
            else:
                Log.warning("帐号密码错误")
                time.sleep(.1)
        else:
            # 错误输入
            Log.warning("错误的选择")
            time.sleep(.1)


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

