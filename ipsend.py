import smtplib
from email.mime.text import MIMEText
import time
# 引入smtplib和MIMEText
import requests
from lxml import etree

host = 'smtp.163.com'
# 设置发件服务器地址
port = 465
# 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
sender = 'lxh731551178@163.com'
# 设置发件邮箱，一定要自己注册的邮箱
pwd = 'lxh19950134572'
# 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
receiver = '731551178@qq.com'
# 设置邮件接收人，可以是QQ邮箱

while True:
    time.sleep(600)
    r = requests.get("https://www.ip.cn/")
    html = etree.HTML(r.text)
    ip = html.xpath('//p/span/span[1]')[0].tail[2:]
    with open("D:\PythonProject\ip.txt","r") as f:
        old_ip = f.readline()
    if ip!=old_ip:
        with open("D:\PythonProject\ip.txt","w") as f:
            f.write(ip)
        try:
            body = ip
            # 设置邮件正文，这里是支持HTML的
            msg = MIMEText(body, 'html')
            # 设置正文为符合邮件格式的HTML内容
            msg['subject'] = 'IP更新'
            # 设置邮件标题
            msg['from'] = sender
            # 设置发送人
            msg['to'] = receiver
            # 设置接收人
            s = smtplib.SMTP_SSL(host, port)
            # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s.login(sender, pwd)
            # 登陆邮箱
            s.sendmail(sender, receiver, msg.as_string())
            # 发送邮件！
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')
    else:
        #print("ip无变化")
        continue




