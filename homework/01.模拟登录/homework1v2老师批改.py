#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 23:40
#---------------
# 编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
#-----------------
'''
总的来说实现的不错
一些小的细节问题或者说是小技巧需要说一下
1、在程序开发中有些值在程序中反复出现，但在程序执行过程中始终不会变化，我们一般的做法是将这样的值定义成常量
在程序的开头定义（大的项目可以通过配置文件的形式定义）这样做的好处是需要修改的时候在一个地方统一修改就可以了
避免修改漏而导致错误。这个程序类比如用来保存用户信息的文件名open('user.txt')以及规定最多输入错误次数3 if userdict[username]['errornum'] >= 3
都可以这样处理。这里print('帐号密码输入错误3次，被锁定，退出')可以这么处理print('帐号密码输入错误%s次，被锁定，退出' %变量名)
2、wirte_data.write(wuserdatestr + '\n')在做字符串处理的时候，尽量不要用+进行拼接，这样做会增加系统资源的消耗和额外开辟内存空间需要的时间
这在大型程序中是很可怕的
3、在对文件进行操作的时候，尤其是读操作，open之前一定要判断文件是否存在，
重复出现的文件可以在开头统一进行判断，不存在则友好的报错退出，而不是用的时候出错抛出不友好的异常信息
'''
userdict = {}
wuserdata = []
login_error_num = 0
print("欢迎来到Python系统，请先登录")

while True:
    username = input("用户名:")
    password = input("密码:")
    #读取用户登陆文件
    user_data = open('user.txt')
    for data in user_data:
        userlist = data.strip()
        userdata = userlist.split(',')
        user_name = userdata[0].strip()
        user_passwd = userdata[1].strip()
        user_lock = userdata[2].strip()
        user_error_num = int(userdata[3].strip())
        userdict[user_name] = {'username':user_name,'password':user_passwd,'lock':user_lock,'errornum':user_error_num}
    user_data.close()

    #判断用户账户是否合法
    if username in userdict.keys():
        if userdict[username]['lock'] == '1':
            print('该账户已被锁定,请联系管理员')
            break
        #判断用户名密码是否匹配
        if username == userdict[username]['username'] and password == userdict[username]['password']:
            print("Success! 登录成功，欢迎",username)
            break
        else:
            userdict[username]['errornum'] += 1
            if userdict[username]['errornum'] >= 3:
                print('帐号密码输入错误3次，被锁定，退出')
                userdict[username]['lock'] = 1
                userdict[username]['errornum'] = 0
            else:
                print('帐号密码错误')
            wirte_data = open('user.txt','w+')
            for t in userdict.values():
                wuserdata = [t['username'],t['password'],str(t['lock']),str(t['errornum'])]
                wuserdatestr = ','.join(wuserdata)
                wirte_data.write(wuserdatestr + '\n')
            wirte_data.close()
            if userdict[username]['errornum'] >= 3:
                break
    else:
        print('帐号或密码错误')



