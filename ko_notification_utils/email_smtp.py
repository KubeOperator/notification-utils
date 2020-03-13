#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/12 
=================================================='''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from ko_notification_utils.response import Response


class Email():

    def __init__(self, address, port, username, password):
        self.username = username
        self.password = password
        self.port = port
        self.address = address
        self.smtp = smtplib.SMTP()

    def send_message(self, receiver, content, title):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.username
        msg['To'] = receiver
        msg['Subject'] = Header(title, 'utf-8').encode()

        try:
            self.smtp.sendmail(self.username, receiver, msg.as_string())
            return Response(code=200, success=True, data={'message': 'send email success!'})
        except smtplib.SMTPException:
            return Response(code=500, success=False, data={'message': 'send email failed!'})

    def quit(self):
        self.smtp.quit()

    def login(self):
        try:
            self.smtp.connect(self.address)
            self.smtp.login(self.username, self.password)
            return Response(code=200, success=True, data={'message': 'login success'})
        except smtplib.SMTPAuthenticationError as e:
            return Response(code=500, success=False, data={'message': str(e.smtp_error.decode())})
