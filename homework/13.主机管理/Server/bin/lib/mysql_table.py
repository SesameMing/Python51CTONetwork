#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-22 17:19
# Version：3.x

#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
#
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# 佛祖保佑    永无bug    心外无法     法外无心






import os
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from bin.lib import setting


class database():
    def __init__(self):
        if os.path.exists(setting.BD_FILE_PATH):
            db_dict = json.load(open(setting.BD_FILE_PATH, 'r'))
            dbstr = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (db_dict.get('db_username'),
                                                                     db_dict.get('db_password'),
                                                                     db_dict.get('db_host'),
                                                                     int(db_dict.get('db_port')),
                                                                     db_dict.get('db_dbname')
                                                                     )
            self.engine = create_engine(dbstr, max_overflow=5, encoding="utf8", convert_unicode=True)
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        else:
            print("链接数据库失败")
            exit(1)

    Base = declarative_base()

    class Admin(Base):
        __tablename__ = 'admin_user'
        id = Column(Integer, primary_key=True)
        username = Column(String(32))
        password = Column(String(32))

    class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        gid = Column(Integer)
        username = Column(String(32))
        password = Column(String(32))

    class Group(Base):
        __tablename__ = 'group'
        id = Column(Integer, primary_key=True)
        title = Column(String(32))
        class_id = Column(String(32))

    class Hostlist(Base):
        __tablename__ = 'host_list'
        id = Column(Integer, primary_key=True)
        ip_name = Column(String(50))
        ip_host = Column(String(50))
        ip_port = Column(Integer)
        class_id = Column(Integer, ForeignKey('host_class.id'))

    class Hostclass(Base):
        __tablename__ = 'host_class'
        id = Column(Integer, primary_key=True)
        title = Column(String(32))

    def create_table(self):
        """
        创建数据表
        :return: none
        """
        self.Base.metadata.create_all(self.engine)

    def setAdminUser(self, user, pwd):
        """
        设置程序管理员
        :param user: 用户名
        :param pwd: 密码
        :return:
        """
        obj = self.Admin(username=user, password=pwd)
        self.session.add(obj)
        self.session.commit()

    def queryAdmin(self, user, pwd):
        """
        验证管理员帐号密码是是否正确
        :param user:
        :param pwd:
        :return:
        """
        try:
            user = self.session.query(self.Admin).filter(self.Admin.username == user, self.Admin.password == pwd).one()
            if int(user.id) > 0:
                return int(user.id)
            else:
                return False
        except:
            return False

    def queryAllHostClass(self):
        """
        管理员查询所有的主机列表
        :return:
        """
        clist = self.session.query(self.Hostclass).all()
        return clist

    def addHostClass(self, name):
        """
        添加主机分组
        :return:
        """
        try:
            obj = self.Hostclass(title=name)
            self.session.add(obj)
            self.session.commit()
            return True
        except:
            return False

    def editHostClass(self, id, name):
        """
        根据id修改主机分组
        :param id: 分组id
        :param name: 新的分组名称
        :return: bool
        """
        try:
            self.session.query(self.Hostclass).filter(self.Hostclass.id == int(id)).update({"title":name})
            self.session.commit()
            return True
        except:
            return False

    def delHostClass(self, id):
        """
        根据id删除分类
        :param id: 分类id
        :return: bool
        """
        try:
            self.session.query(self.Hostclass).filter(self.Hostclass.id == int(id)).delete()
            self.session.commit()
            return True
        except:
            return False

    def queryAllHostList(self):
        """
        查询所有的主机
        :return: 主机列表
        """
        list = self.session.query(self.Hostlist).all()
        return list

    def addHost(self, ip_name, class_id, ip_host):
        """
        向数据库插入一条记录
        :param hostname: 昵称
        :param cid: 分类id
        :param hostip: 主机ip
        :return: bool
        """
        try:
            obj = self.Hostlist(ip_host=ip_host, class_id=class_id, ip_name=ip_name)
            self.session.add(obj)
            self.session.commit()
            return True
        except:
            return False

    def editHost(self, id, ip_name, ip_host):
        """
        根据id 修改主机信息
        :param id: 主机id
        :param ip_name: 备注昵称
        :param ip_host: ip
        :return:
        """
        updict = {}
        if ip_name:
            updict['ip_name'] = ip_name
        if ip_host:
            updict['ip_host'] = ip_host
        try:
            self.session.query(self.Hostlist).filter(self.Hostlist.id == int(id)).update(updict)
            self.session.commit()
            return True
        except:
            return False

    def delHost(self, id):
        """
        删除主机
        :param id: 主机id
        :return: bool
        """
        try:
            self.session.query(self.Hostlist).filter(self.Hostlist.id == int(id)).delete()
            self.session.commit()
            return True
        except:
            return False

    def queryAllUserGroup(self):
        """
        查询所有用户分组
        :return: list
        """
        ret = self.session.query(self.Group).all()
        return ret

    def addUserGroup(self, title, class_id):
        """
        添加用户分组
        :param title: 用户分组名称
        :param class_id: 用户分组所包含的主机组
        :return:
        """
        try:
            obj = self.Group(title=title, class_id=class_id)
            self.session.add(obj)
            self.session.commit()
            return True
        except:
            return False

    def editUserGroup(self, id, title, class_id):
        """
        编辑用户分组
        :param id: 分组id
        :param title: 分组名称
        :param class_id: 主机分组id
        :return:
        """
        updict = {}
        if title:
            updict['title'] = title
        if class_id:
            updict['class_id'] = class_id
        try:
            self.session.query(self.Group).filter(self.Group.id == int(id)).update(updict)
            self.session.commit()
            return True
        except:
            return False

    def delUserGroup(self, id):
        """
        根据id删除用户分组
        :param id:
        :return:
        """
        try:
            self.session.query(self.Group).filter(self.Group.id==int(id)).delete()
            self.session.commit()
            return True
        except:
            return False

    def queryAllUser(self):
        """
        查询所有的用户
        :return:
        """
        ret = self.session.query(self.User, self.Group).filter(self.User.gid == self.Group.id).all()
        return ret

    def addUser(self, username, password, gid):
        """
        添加用户
        :param username:
        :param password:
        :param gid:
        :return:
        """
        try:
            obj = self.User(username=username, password=password, gid=gid)
            self.session.add(obj)
            self.session.commit()
            return True
        except:
            return False

    def editUser(self, id, password, gid):
        """
        修改用户
        :param id: 用户id
        :param password: 新密码
        :param gid: 新用户组
        :return:
        """
        updict = {}
        if password:
            updict['password'] = password
        if gid:
            updict['gid'] = gid
        try:
            self.session.query(self.User).filter(self.User.id == int(id)).update(updict)
            self.session.commit()
            return True
        except:
            return False

    def delUser(self, id):
        """
        删除用户
        :param id: 用户id
        :return: bool
        """
        try:
            self.session.query(self.User).filter(self.User.id == int(id)).delete()
            self.session.commit()
            return True
        except:
            return False

    def queryUser(self, username, password):
        """
        普通用户登录查询
        :param username:
        :param password:
        :return:
        """
        try:
            user = self.session.query(self.User).filter(self.User.username == username, self.User.password == password).one()
            if int(user.id) > 0:
                return int(user.id)
            else:
                return False
        except:
            return False

    def showUserHost(self, id):
        """
        显示用户下面的主机
        :param id: 用户id
        :return:
        """
        ret = self.session.query(self.Hostlist).filter(self.User.id == id and self.User.gid == self.Group.id and self.Group.class_id == self.Hostlist.class_id).all()
        return ret

    def gethost(self, id):
        """
        通过id获取ip
        :param id: 主机id
        :return:
        """
        host = []
        hostlist = self.session.query(self.Hostlist).filter(self.Hostlist.id == int(id)).one()
        host.append(hostlist.ip_host)
        return host










