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

    def send_message(self, receiver, content):

        data = {
            "msgtype": "text",
            "text": {
                "content": str(content)
            },
            "at": {
                "atMobiles": [
                    receiver
                ],
                "isAtAll": False
            }
        }

        timestamp = int(round(time.time() * 1000))
        secret_enc = bytes(self.secret, 'utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = bytes(string_to_sign, 'utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = parse.quote_plus(base64.b64encode(hmac_code))
        url = "https://oapi.dingtalk.com/robot/send?access_token={0}&timestamp={1}&sign={2}".format(self.webhook,
                                                                                                    timestamp, sign)

        try:
            result = requests.post(url, data=json.dumps(data), headers=self.headers, timeout=20)
            return Response(code=result.status_code, data=json.loads(data))
        except Exception as e:
            return Response(code=400, data=json.loads(data))
