#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/11 
=================================================='''
import requests
import json
import logging
from ko_notification_utils.response import Response

logging.getLogger("requests").setLevel(logging.ERROR)

class WorkWeiXin():
    headers = {
        "Content-Type": "application/json",
    }

    def __init__(self, corp_id, corp_secret, agent_id):
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.agent_id = agent_id

    def send_message(self, receivers, content, token, type):
        data = {
            "msgtype": type,
            "touser": receivers,
            "agentid": self.agent_id
        }
        data[type] = content
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
        result = requests.post(url=url, headers=self.headers, json=data)
        if json.loads(result.text)['errcode'] == 0:
            return Response(code=result.status_code, success=True, data=json.loads(result.text))
        else:
            return Response(code=500, success=False, data=json.loads(result.text))

    def send_markdown_msg(self, receivers, content, token):
        msg = content.get('content', '')
        markdown = {
            "content": msg
        }
        return self.send_message(receivers, markdown, token, 'markdown')

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(self.corp_id,
                                                                                            self.corp_secret)
        result = requests.get(url=url, headers=self.headers)
        if json.loads(result.text)['errcode'] == 0:
            return Response(code=result.status_code, success=True, data=json.loads(result.text))
        else:
            return Response(code=500, success=False, data=json.loads(result.text))
