#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-29 0:36

# 打开文件
# f = open('db', 'r')  # 只读
# f = open('db', 'w')  # 只写
# f = open('db', 'x')  # 文件存在，报错；不存在，创建并只写
# f = open('db', 'a')  # 追加


f = open('db', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()

# 如果打开方式带有b open('xxx','rb') 那么读取或者只能写入字节



# 操作文件
# 通过源码查看功能
# 关闭文件
# f.close()






#
# with open('db') as f:
#     pass

