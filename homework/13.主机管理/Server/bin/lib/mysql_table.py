#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-22 17:19
# Version：3.x

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
                                                                     db_dict.get('db_name')
                                                                     )
            self.engine = create_engine(dbstr, max_overflow=5, encoding="utf8", convert_unicode=True)
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        else:
            print("链接数据库失败")
            exit(1)

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        usernae = Column(String(32))
        password = Column(String(32))

    class Group(Base):
        __tablename__ = 'group'
        id = Column(Integer, primary_key=True)
        title = Column(String(32))
        class_id = Column(String(32))

    class UserToGroup(Base):
        __tablename__ = 'user_to_group'
        id = Column(Integer, primary_key=True)
        uid = Column(Integer, ForeignKey('user.nd'))
        groupid = Column(Integer, ForeignKey('group.nid'))

    class Hostlist(Base):
        __tablename__ = 'host_list'
        id = Column(Integer, primary_key=True)
        ip_host = Column(String(50))
        ip_port = Column(Integer)
        class_id = Column(Integer, ForeignKey('host_class.nid'))

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






