#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText


class MailModel:

    def __init__(self):
        self.mail_host = "smtp.163.com"
        self.mail_user = "username"
        self.mail_pass = "password"
        self.postfix = "163.com"

    def send_mail(self, to_list, sub, content):
        me = "hello"+"<"+self.mail_user+"@"+self.postfix+">"
        msg = MIMEText(content, _subtype = 'html', _charset = 'utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ';'.join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False

    def start(self):
        print 'hello world'

mailto_list=["xxx@qq.com", "xxx@163.com"]

mail = MailModel()
if mail.send_mail(mailto_list, 'testing', "测试邮件"):
    print "发送成功"
else:
    print "发送失败"
