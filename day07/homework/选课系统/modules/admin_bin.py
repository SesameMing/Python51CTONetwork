#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-27 15:07

import pickle
from conf import setting

def main():
    print("main方法")


def login():
    pass


def run():
    print(setting.TEACHER_DIR_FILE)
    if login():
        main()

if __name__ == '__main__':
    main()
