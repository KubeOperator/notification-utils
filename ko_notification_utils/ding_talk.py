import requests
import json
import time
import hmac
import hashlib
import base64
from urllib import parse

from ko_notification_utils.response import Response


class DingTalk():
    headers = {
        "Content-Type": "application/json"
    }

    def __init__(self, webhook, secret):
        self.webhook = webhook
        self.secret = secret

    def send_message(self, receivers, content , type):

        if type is None:
            type = 'text'
        else:
            type =  type

        data = {
            "msgtype": type,
            "at": {
                "atMobiles": receivers,
                "isAtAll": False
            }
        }
        data[type] = content

        timestamp = int(round(time.time() * 1000))
        secret_enc = bytes(self.secret, 'utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = bytes(string_to_sign, 'utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = parse.quote_plus(base64.b64encode(hmac_code))
        url = "{0}&timestamp={1}&sign={2}".format(self.webhook, timestamp, sign)

        result = requests.post(url, data=json.dumps(data), headers=self.headers)

        if json.loads(result.text)['errcode'] == 0:
            return Response(code=result.status_code, success=True, data=json.loads(result.text))
        else:
            return Response(code=500, success=False, data=json.loads(result.text))

    def send_markdown_msg(self, receivers, content):
        markdown = {
            "title":content.get('title',''),
            "text":content.get('text','')
        }
        return self.send_message(receivers=receivers,content=markdown,type='markdown')

    def send_text_msg(self, receivers, content):
        text = {
            "content":content
        }
        return  self.send_message(receivers=receivers,content=text,type='text')

