#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fetch(backend):
    # backend = "www.oldboy.org"
    result = []
    with open('ha.conf', 'r', encoding='utf-8') as f:
        flag = False
        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith("backend"):
                flag = False
                break
            if flag and line.strip():
                result.append(line.strip())

    return result

# ret = fetch("www.oldboy.org")
# print(ret)

def add(backend, record):
    # 思路一：
    # 思路二：
    # 先检查记录存不存
    record_list = fetch(backend)
    if not record_list:
        # backend不存在
        with open('ha.conf', 'r') as old, open("new.conf", 'w') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + backend + "\n")
            new.write(" " * 8 + record + "\n")
    else:
        # backend存在
        if record in record_list:
            # record已经存在
            # import shutil
            # shutil.copy("ha.conf", 'new.conf')
            pass
        else:
            # backend存在,record不存在
            record_list.append(record)
            with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        flag = True
                        new.write(line)
                        for new_line in record_list:
                            new.write(" "*8 + new_line + "\n" )
                        continue
                    if flag and line.strip().startswith("backend"):
                        flag = False
                        new.write(line)
                        continue
                    if line.strip() and not flag:
                        new.write(line)


bk = "www.oldboy.org"
rd = "server 100.1.7.49 100.1.7.49 weight 20 maxconn 30"
add(bk, rd)
# s = "[11,22,33,44,5, 66]"
# s = '{"k1":"v1"}'
# print(type(s),s)
#
# import json
# n = json.loads(s) # 将一个字符串，转换成python的基本数据类型; 注意：字符串形式的字典'{"k1":"v1"}'内部的字符串必须是 双引号
# print(type(n), n)
# import json
# r = input("input:")
# dic = json.loads(r)
# bk = dic['backend']
# rd = "server %s %s weight %d maxconn %d" %(dic['record']['server'],
#                                            dic['record']['server'],
#                                            dic['record']['weight'],
#                                            dic['record']['maxconn'])
