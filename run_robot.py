import os
import time
import win32com.client as win32

# RUN_PATH = os.path.dirname(os.path.abspath(__file__))
# os.system("cd" + RUN_PATH)
'获取当前路径'
path1 = os.getcwd()
file_path1 = path1.split(":")[0]

'切换到需要执行的目录'
os.system(file_path1+":")
os.system("cd "+path1)


def sendmail():
    sub = 'DM open api test'  # 标题
    body = 'Hi All:\r\n DM 接口测试报告'  # 内容
    outlook = win32.Dispatch('outlook.application')
    receivers = ['chencany@yealink.com']  # 收件人
    mail = outlook.CreateItem(0)
    if len(receivers) == 1:
        mail.To = receivers[0]
    else:
        mail.To = ";".join(receivers)
    mail.Subject = sub
    mail.Body = body
    file_path = os.getcwd()
    mail.Attachments.Add(file_path + r'robot_report\log.html')
    mail.Attachments.Add(file_path + r'robot_report\output.xml')
    mail.Attachments.Add(file_path + r'robot_report\report.html')
    mail.Send()


if __name__ == '__main__':
    '''配置参数在cfg.py,发送邮件需要本地先登录'''
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # report_path = r"E:\PycharmProjects\OPEN_API\robot_report"
    report_path = os.getcwd() + r"\robot_report"
    os.system(f"robot  -d {report_path} --pythonpath  . open_api")  # 执行全部，不执行的需要注释掉
    # os.system(f"robot  -d {report_path}  -i test1   --pythonpath .  open_api")
    os.system(report_path + r'\log.html')  # 打开测试报告
    # sendmail()  # 需要发送邮件启用
