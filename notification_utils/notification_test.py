import unittest
from notification_utils.ding_talk import DingTalk

class NotificationTest(unittest.TestCase):

    def test_ding_talk(self):
        ding_talk = DingTalk('toekn')
        success = ding_talk.send_message('','message','')
        print(success)


if __name__ == '__main__':
    unittest.main()
