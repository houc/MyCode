import smtplib
import os
import sys

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from config_path.path_file import read_file
from . Yaml import MyConfig
from . HtmlDataHandle import AmilSupport


class Email:
    def __init__(self):
        self.Mail = smtplib.SMTP()
        self.contents = MIMEMultipart()
        self.sender = MyConfig('send_account').send_email
        self.sender_password = MyConfig('send_password').send_email
        self.server = MyConfig('server').send_email
        self.port = MyConfig('port').send_email
        self.receiver = MyConfig('receiver').send_email
        self.cc = MyConfig('CC').send_email
        self.title_name = MyConfig('project_name').excel_parameter
        self.title = MyConfig('science').excel_parameter
        self.img_path = read_file('img', 'html.png')
        self.excel_path = read_file('report', 'case_info.xlsx')

    def _send_title_msg(self, url, case_name):
        self._send_content(url)
        self._send_enclosure(case_name)
        self._send_file()
        self.contents['from'] = Header(self.sender)
        self.contents['to'] = Header(', '.join(self.receiver))
        self.contents['cc'] = Header(', '.join(self.cc))
        self.contents['subject'] = Header(f'{self.title_name + self.title}自动化测试报告')
        return self.contents

    def _send_content(self, url):
        link_url = f"""<a href="{url}" target="_blank">点击此处在线查看测试报告</a><img alt="" src="cid:image1"/>"""
        self.contents.attach(MIMEText(link_url, 'html', 'utf8'))

    def _send_enclosure(self, case_name):
        AmilSupport(case_name)
        sys.stderr.write('邮件中的截图统计已完成，正在发送邮件...\n')
        if os.path.exists(self.img_path):
            img = MIMEImage(open(self.img_path, 'rb').read())
            img.add_header('Content-ID', '<image1>')
            self.contents.attach(img)

    def _send_file(self):
        att = MIMEText(open(self.excel_path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="info.xlsx"'
        self.contents.attach(att)

    def sender_email(self, url, case_name):
        try:
            content = self._send_title_msg(url, case_name)
            self.Mail.connect(host=self.server, port=self.port)
            self.Mail.login(self.sender, self.sender_password)
            self.Mail.sendmail(self.sender, self.receiver + self.cc, content.as_string())
            self.Mail.quit()
            if self.cc:
                sys.stderr.write(f'抄送{"、".join(self.cc)}成功; 发送{"、 ".join(self.receiver)}成功\n')
            else:
                sys.stderr.write(f'给{"、 ".join(self.receiver)}邮件发送成功\n')
        except smtplib.SMTPException:
            if self.cc:
                sys.stderr.write(f'抄送{"、".join(self.cc)}失败; 发送{"、 ".join(self.receiver)}失败！\n')
            else:
                sys.stderr.write(f'给{"、 ".join(self.receiver)}邮件发送失败\n')
        sys.stderr.flush()


if __name__ == '__main__':
    Email().sender_email('http://www.baidu.com', '')