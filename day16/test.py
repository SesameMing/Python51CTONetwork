#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-12-14 13:09

import os
import time
datestr = time.strftime("%Y-%m-%d", time.localtime())
filename = []
dirname = '处理后的文件'  # 处理文件目录名称
for i in os.listdir():
    if os.path.isfile(i):
        if os.path.join(os.getcwd(), i) != os.path.abspath(__file__):
            filename.append(i)

for oldfilename in filename:
    newfilename = datestr + '_处理_' + oldfilename

    if not os.path.exists(os.path.join(os.getcwd(), dirname)):
        os.mkdir(os.path.join(os.getcwd(), dirname))

    with open(os.path.join(os.getcwd(), oldfilename)) as old, open(open(os.path.join(os.getcwd(), dirname, newfilename))) as new:
        try:
            f = True
            for line in old:
                if line.strip().startswith("[SOFT BIN MAP]") and f is True:
                    f = False
                    continue
                elif line.strip().startswith("[EXTENSION]") and f is False:
                    f = True
                    continue
                elif f is False:
                    new.write(line)
        except Exception as ex:
            pass
        print("处理完文件【%s】" % oldfilename)




