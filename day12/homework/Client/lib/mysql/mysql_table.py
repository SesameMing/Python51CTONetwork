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
            dbstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (db_dict.get('db_username'),
                                                        db_dict.get('db_password'),
                                                        db_dict.get('db_host'),
                                                        int(db_dict.get('db_port')),
                                                        db_dict.get('db_name')
                                                        )
            self.engine = create_engine(dbstr, max_overflow=5)
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
        ip = Column(String(32))
        port = Column(Integer)
        uname = Column(String(32))
        passwd = Column(String(32))

    def init(self):
        """
        创建数据表
        :return:
        """
        self.Base.metadata.create_all(self.engine)

    def setadmin(self, username, password):
        obj = self.User(name=username, password=password)
        self.session.add(obj)
        self.session.commit()

    def yzuser(self, username, password):
        try:
            user = self.session.query(self.User).filter(self.User.name == username, self.User.password == password).one()
            if int(user.id) > 0:
                self.user_id = user.id
                return True
            else:
                return False
        except:
            return False