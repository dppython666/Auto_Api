# 这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑。
import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, username, password, recv, title, content,
                 file=None, ssl=False,
                 email_host="smtp.163.com", port=25, ssl_port=465):

        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.ssl = ssl
        self.email_host = email_host
        self.port = port
        self.ssl_port = ssl_port

    def send_email(self):
        msg = MIMEMultipart()
        # 发送内容对象
        if self.file:  # 处理附件
            file_name = os.path.split(self.file)[-1]  # 只取文件名
            try:
                f = open(self.file, "rb").read()
            except Exception as e:
                raise Exception("附件无法打开！")
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Ccontent-Type"] = "application/octet-stream"

            new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
            # 这里是处理文件名为中文名
            att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
            msg.attach(att)

        msg.attach(MIMEText(self.content))  # 邮件正文内容
        msg["Subject"] = self.title  # 邮件主题
        msg["From"] = self.username  # 发送者账号
        msg["To"] = ",".join(self.recv)  # 接收者账号
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器对象
        self.smtp.login(self.username, self.password)
        try:
            self.smtp.sendmail(self.username,  self.recv, msg.as_string())
            pass
        except Exception as e:
            print("出现错误", e)
        else:
            print("发送成功！")
        self.smtp.quit()


if __name__ == '__main__':

    m = SendEmail(
        username="test_ark@163.com",
        password="DPTSUXBYYUEFTGME",
        recv=["zzjbj86@163.com"],
        title="接口自动化测试报告",
        content="测试发送邮件",
        file=r"C:\Users\Asus\Desktop\Auto_Test\result\report.html",
        ssl=True,
    )
    m.send_email()
