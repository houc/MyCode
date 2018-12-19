import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from model.Yaml import MyYaml
from config_path.path_file import read_file


class Email:
    def __init__(self):
        self.Mail = smtplib.SMTP()
        self.contents = MIMEMultipart()
        self.sender = MyYaml('send_account').send_email
        self.sender_password = MyYaml('send_password').send_email
        self.server = MyYaml('server').send_email
        self.receiver = MyYaml('receiver').send_email
        self.title_name = MyYaml('project_name').excel_parameter
        self.title = MyYaml('science').excel_parameter
        self.img_path = read_file('img','logo.png')
        self.excel_path = read_file('report','ExcelReport.xlsx')

    def _send_title_msg(self):
        """发送表头信息"""
        self._send_content()
        self._send_file()
        self.contents['from'] = Header(self.sender)
        self.contents['to'] = Header(','.join(self.receiver))
        self.contents['subject'] = Header('{}自动化测试报告'.format(self.title_name + self.title))
        return self.contents

    def _send_content(self):
        """发送具体内容"""
        img = MIMEImage(open(self.img_path,'rb').read())
        img.add_header('Content-ID', '<image1>')
        link_url = """
        <b><i><font size="3" color="red"><a href="{}" target="_blank" class="mnav">点击此处在线查看测试报告</a></font>\
        </i></b><img alt="" src="cid:image1"/>
        """.format('http://www.baidu.com')
        content = MIMEText(link_url,'html')
        self.contents.attach(content)
        self.contents.attach(img)
        return self.contents

    def _send_file(self):
        """发送带附件的内容"""
        att = MIMEText(open(self.excel_path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="excel.xls"'
        self.contents.attach(att)
        return self.contents

    def sender_email(self):
        """发送邮件"""
        try:
            content = self._send_title_msg()
            self.Mail.connect(self.server)
            self.Mail.login(self.sender,self.sender_password)
            self.Mail.sendmail(self.sender,self.receiver,content.as_string())
            self.Mail.quit()
            print('给{}邮件发送成功'.format(','.join(self.receiver)))
        except smtplib.SMTPException:
            print('给{}邮件发送失败'.format(','.join(self.receiver)))



if __name__ == '__main__':
    Email().sender_email()