#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

"""
def sendmail():
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
        msg['To'] = formataddr(["走人",'424662508@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("wptawy@126.com", "WW.3945.5")
        server.sendmail('wptawy@126.com', ['3628905@qq.com',], msg.as_string())
        server.quit()
    except:
        # 发送失败
        return "失败"
    else:
        # 发送成功
        return "cc"
ret = sendmail()


print(ret)
if ret == "cc":
    print('发送成功')
else:
    print("发送失败")
"""
# print(123)

# def f1():
#     print(123)
#     # 在函数中，一旦执行return，函数执行过程立即终止
#     return "111"
#     print(456)
#
# r = f1()
# print(r)

# def f2():
#     print(123)
#
# r = f2()
# print(r)
# 形式参数
"""
def sendmail(xxoo, content):
    # xxoo = alex
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
        msg['To'] = formataddr(["走人",'424662508@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("wptawy@126.com", "WW.3945.59")
        server.sendmail('wptawy@126.com', [xxoo,], msg.as_string())
        server.quit()
    except:
        # 发送失败
        return "失败"
    else:
        # 发送成功
        return "cc"


while True:
    em = input("请输入邮箱地址:")
    result = sendmail(em, "SB")
    if result == "cc":
        print("发送成功")
    else:
        print("发送失败")

"""
"""
def send(xxoo, content, xx="OK"):
    print(xxoo, content, xx)
    print("发送邮件成功:", xxoo, content)
    return True

while True:
    em = input("请输入邮箱地址:")
    result = send(em, "SB", "ok")
    if result == True:
        print("发送成功")
    else:
        print("发送失败")
"""
"""
def send(xxoo, content, xx="OK"):
    print(xxoo, content, xx)
    # print("发送邮件成功:", xxoo, content)
    return True

send('alex', "sb")
send('alex', "sb", "BB")
"""

# def send(xxoo, content):
#     print(xxoo, content)
#     # print("发送邮件成功:", xxoo, content)
#     return True
#
# send(content="alex", xxoo="sb")

# 1、普通参数（严格按照顺序，将实际参数赋值给形式参数）
# 2、默认参数（必须放置在参数列表的最后）
# 3、指定参数（将实际参数赋值给制定的形式参数）
# 4、动态参数：
#        *      默认将传入的参数，全部放置在元组中， f1(*[1`1,22,33,44])
#        **     默认将传入的参数，全部放置在字典中   f1(**{"kl":"v1", "k2":"v2"})
# 5、万能参数,   *args,**kwargs

# str.format()
# str format格式化输出
# "%s %d"

# s1 = "i am {0}, age {1}".format("alex", 18)
# print(s1)
# s2 = "i am {0}, age {1}".format(*["alex", 18])
# print(s2)

# s1 = "i am {name}, age {age}".format(name='alex', age=18)
# print(s1)
#
# dic = {'name': 'alex', "age": 18}
# s2 = "i am {name}, age {age}".format(**dic)
# print(s2)

# "asd".format()

# def f1(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# f1(k1="v1")

# def f1(*args):
#     # args = (11,)
#     # args = ([11,22,"alex", "hhhh"],"12")
#     print(args, type(args))

# f1(11,22,33,44)
# li = [11,22,33,44]
# f1(*li)


# def f1(**args):
#     # args = (11,)
#     # args = ([11,22,"alex", "hhhh"],"12")
#     print(args, type(args))

# f1(n1="alex", n2=18)
# dic = {'k1': "v1", "k2":"v2"}
# f1(kk=dic)

# dic = {'k1': "v1", "k2":"v2"}
# f1(**dic)



# f1(11)
# li = [11,22,"alex", "hhhh"]
# f1(li, '12')
# li = [11,22,"alex", "hhhh"]
# f1(li)
# f1(*li)
# li = "alex"
# f1(*li)



# def send(xxoo, xx, content="OK", oo="xxx"):
#     print(xxoo, content, xx)
#     # print("发送邮件成功:", xxoo, content)
#     return True

# send('alex', "sb")
# send('alex', "sb", "BB")

# def f1(a1, a2):
#     return a1 + a2
#
# def f1(a1, a2):
#     return a1 * a2
#
# ret = f1(8, 8)
# print(ret)

# name = "alex"
# name = "eric"
# print(name)

# def f1(a1):
#     a1.append(999)
#
# li = [11,22,33,44]
# f1(li)
#
# print(li)


# 全局变量
"""
def f1():
    name = "alex"
    print(name)

def f2():
    print(name)
"""
# 全局变量，所有作用域都可读
# 对全局变量进行【重新赋值】，需要global
# 特殊：列表字典，可修改，不可重新赋值

# 笑嘻嘻笑嘻嘻
NAME = None

def f1():
    age = 18
    global NAME # 表示，name是全局变量
    # NAME = "123"

    print(age, NAME)

def f2():
    age = 19
    print(age, NAME)
f1()
f2()

















