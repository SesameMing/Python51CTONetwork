#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-21 12:36
import os
import time
import logging
from conf import setting
USER_LOGIN_STATUS = {'login': False, 'username': None}


def setloggin():
    logger = logging.getLogger("客户端程序")
    if not logging._handlers:
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s %(levelname)s] %(message)s'))
        logger.addHandler(ch)
    return logger
Log = setloggin()




def main():
    print("run")


def login():
    Log.info("用户登录")
    time.sleep(.1)
    username = input("请输入账号：").strip()
    password = input("请输入密码：").strip()
    if os.path.exists(os.path.join(setting.USER_DIR_PATH, username)):
        pass




def run():
    Log.info("启动")
    if login():
        main()

if __name__ == '__main__':
    main()