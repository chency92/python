import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

'获取当前路径'
path1 = os.getcwd()
file_path = path1.split(":")[0]

'切换到需要执行的目录'
os.system(file_path+":")
os.system("cd "+path1)


def send_mail():
    sender = 'chencany@yealink.com'
    password = 'Yl@2019'
    receivers = ['chencany@yealink.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 创建一个带附件的实例
    message = MIMEMultipart()
    # message['From'] = Header("测试四部", 'utf-8')
    # message['To'] = Header("测试", 'utf-8')
    subject = '测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('DM测试报告', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 report.html 文件
    att1 = MIMEText(open(f"{path1}\\report.html", 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att1)
    # 构造附件2，传送当前目录下的 output.xml 文件
    att2 = MIMEText(open(f"{path1}\\output.xml", 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="output.xml"'
    message.attach(att2)
    # 构造附件3，传送当前目录下的 log.html 文件
    att3 = MIMEText(open(f"{path1}\\log.html", 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="log.html"'
    message.attach(att3)

    try:
        server = smtplib.SMTP('smtp.exmail.qq.com', 25)
        server.login(sender, password)
        server.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
