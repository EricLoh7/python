# !/usr/bin/env python
# -*- coding:utf-8 -*-
from email.header import  Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#以发送方为网易邮箱为例，必须开通SMTP功能
from_addr = 'xxxxxxx@163.com'
#客户端授权密码
password = 'xxxxxxxx'
to_addr = 'xxxxxxxxx@xxx.com'
#网易邮箱服务器地址
smtp_server = 'smtp.163.com'  

#设置邮件信息
msg = MIMEText('邮件正文','plain','utf-8')
msg['FROM'] = from_addr
msg['TO'] = to_addr
msg['Subject'] = Header('邮件主题','utf-8').encode()

#发送邮件
server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
