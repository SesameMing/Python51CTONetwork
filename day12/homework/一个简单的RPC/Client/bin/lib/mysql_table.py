#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-10 12:05
# Version：3.x
import os
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from config import setting


class initdatebase():
    def __init__(self):
        if os.path.exists(setting.BD_FILE_PATH):
            db_dict = json.load(open(setting.BD_FILE_PATH, 'r'))
            dbstr = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (db_dict.get('db_username'),
                                                        db_dict.get('db_password'),
                                                        db_dict.get('db_host'),
                                                        int(db_dict.get('db_port')),
                                                        db_dict.get('db_name')
                                                        )
            self.engine = create_engine(dbstr, max_overflow=5, encoding="utf8", convert_unicode=True)
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        else:
            print("创建数据表异常")
            return False
    Base = declarative_base()
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))
        password = Column(String(32))

    class Classify(Base):
        __tablename__ = 'classify'
        id = Column(Integer, primary_key=True)
        classname = Column(String(32))

    class Hostlist(Base):
        __tablename__ = 'hostlist'
        id = Column(Integer, primary_key=True)
        cid = Column(Integer)
        nickname = Column(String(32))
        ip = Column(String(32))
        port = Column(Integer)
        uname = Column(String(32))
        passwd = Column(String(32))

    def init(self):
        """
        创建数据表
        :return: none
        """
        self.Base.metadata.create_all(self.engine)

    def setadmin(self, username, password):
        """
        设置帐号密码
        :param username: 帐号
        :param password: 密码
        :return: bool
        """
        obj = self.User(name=username, password=password)
        self.session.add(obj)
        self.session.commit()
        return True

    def yzuser(self, username, password):
        """
        验证用户帐号密码正确性
        :param username: 帐号
        :param password: 密码
        :return: bool
        """
        try:
            user = self.session.query(self.User).filter(self.User.name == username, self.User.password == password).one()
            if int(user.id) > 0:
                self.user_id = user.id
                return True
            else:
                return False
        except:
            return False

    def setHostfz(self, classname):
        """
        添加分组
        :param classname: 分组名称
        :return: bool
        """
        obj = self.Classify(classname=classname)
        self.session.add(obj)
        self.session.commit()
        return True

    def showHostfz(self):
        """
        显示分组列表
        :return: 分组列表
        """
        hostfz = self.session.query(self.Classify).all()
        return hostfz

    def editHostfz(self, id, chassname):
        """
        修改分类名称
        根据id号修改 分类名称
        :param id: 分组的id
        :param chassname: 新的分组名称
        :return: bool
        """
        self.session.query(self.Classify).filter(self.Classify.id == int(id)).update({"classname": chassname})
        self.session.commit()
        return True

    def delHostfz(self, id):
        """
        删除分类
        根据id号 删除 分类名称
        :param id: 分类的id
        :return: bool
        """
        self.session.query(self.Classify).filter(self.Classify.id == int(id)).delete()
        self.session.commit()
        return True

    def showHost(self):
        """
        显示主机列表
        :return: 主机列表
        """
        hostlist = self.session.query(self.Hostlist).all()
        return hostlist

    def addHost(self, name, cid, ip):
        """
        添加主机
        :param name: 主机昵称
        :param cid: 主机分组id
        :param ip: 主机ip地址
        :return: bool
        """
        obj = self.Hostlist(nickname=name, cid=cid, ip=ip)
        self.session.add(obj)
        self.session.commit()
        return True

    def editHost(self, id, name, ip):
        """
        根据id号修改主机信息
        :param id: 主机id
        :param name: 主机昵称
        :param ip: 主机ip
        :return: bool
        """
        updict = {}
        if name:
            updict['nickname'] = name
        if ip:
            updict['ip'] = ip
        self.session.query(self.Hostlist).filter(self.Hostlist.id == int(id)).update(updict)
        self.session.commit()
        return True

    def delHost(self, id):
        """
        删除主机
        :param id: 主机id
        :return:
        """
        self.session.query(self.Hostlist).filter(self.Hostlist.id == int(id)).delete()
        self.session.commit()
        return True

    def classTohost(self, id):
        """
        根据分类id获取主机列表
        :param id:
        :return:
        """
        hostlist = self.session.query(self.Hostlist).filter(self.Hostlist.cid == int(id)).all()
        return hostlist

    def gethost(self, id):
        host = []
        hostlist = self.session.query(self.Hostlist).filter(self.Hostlist.id == int(id)).one()
        host.append(hostlist.ip)
        return host