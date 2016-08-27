#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-28 0:15

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('大明 这是一封测试邮件', 'plain', 'utf-8')
msg['From'] = formataddr(["大明", '15171888087@163.com'])
msg['To'] = formataddr(["大明api", 'admin@v-api.com'])
msg['Subject'] = "python邮件函数测试"

server = smtplib.SMTP("smtp.163.com", 25)
server.login("15171888087@163.com", "7833922")
server.sendmail('15171888087@163.com', ['admin@v-api.com', ], msg.as_string())
server.quit()