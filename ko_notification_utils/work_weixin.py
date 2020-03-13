#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/11 
=================================================='''
import requests
import json
from ko_notification_utils.response import Response


class WorkWinXin():
    headers = {
        "Content-Type": "application/json",
    }

    def __init__(self, corp_id, corp_secret, agent_id):
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.agent_id = agent_id

    def send_message(self, receiver, content, token):
        data = {
            "msgtype": "text",
            "touser": receiver,
            "agentid": self.agent_id,
            "text": {
                "content": content
            }
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
        result = requests.post(url=url, headers=self.headers, json=data)
        if json.loads(result.text)['errcode'] == 0:
            return Response(code=result.status_code, success=True, data=json.loads(result.text))
        else:
            return Response(code=500, success=False, data=json.loads(result.text))

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(self.corp_id,
                                                                                            self.corp_secret)
        result = requests.get(url=url, headers=self.headers)
        if json.loads(result.text)['errcode'] == 0:
            return Response(code=result.status_code, success=True, data=json.loads(result.text))
        else:
            return Response(code=500, success=False, data=json.loads(result.text))
