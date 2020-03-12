#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/11 
=================================================='''
import requests
import json
from notification_utils.response import Response


class WorkWinXin():
    headers = {
        "Content-Type": "application/json",
    }

    def send_message(self, content, token, agent_id, touser):
        data = {
            "msgtype": "text",
            "touser": touser,
            "agentid": agent_id,
            "text": {
                "content": content
            }
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
        result = requests.post(url=url, headers=self.headers, json=data)
        return Response(code=result.status_code, data=json.loads(result.text))

    def get_token(self, corp_id, corp_secret):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(corp_id, corp_secret)
        result = requests.get(url=url, headers=self.headers)
        return Response(code=result.status_code, data=json.loads(result.text))
