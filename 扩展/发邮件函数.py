#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-28 0:15

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def sendmail():

    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["SemaseMing", '发件邮箱'])
    msg['To'] = formataddr(["SemaseMing", '收件邮箱'])
    msg['Subject'] = "python邮件函数测试"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("发件邮箱", "密码")
    server.sendmail('发件邮箱', ['收件邮箱', ], msg.as_string())
    server.quit()
