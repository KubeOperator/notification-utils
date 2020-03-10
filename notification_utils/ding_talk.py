import requests
import json
import time
import hmac
import hashlib
import base64
from urllib import parse

class DingTalk():
    headers = {
        "Content-Type": "application/json"
    }

    def __init__(self, webhook,secret):
        self.webhook = webhook
        self.secret = secret

    def send_message(self, user, message):

        data = {
            "msgtype": "text",
            "text": {
                "content": str(message)
            },
            "at": {
                "atMobiles": [
                    user
                ],
                "isAtAll": False
            }
        }

        timestamp = int(round(time.time() * 1000))
        secret_enc = bytes(self.secret,'utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = bytes(string_to_sign,'utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = parse.quote_plus(base64.b64encode(hmac_code))

        url = "https://oapi.dingtalk.com/robot/send?access_token={0}&timestamp={1}&sign={2}".format(self.webhook,timestamp,sign)
        try:
            response = requests.post(url, data=json.dumps(data), headers=self.headers, timeout=20)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            return False