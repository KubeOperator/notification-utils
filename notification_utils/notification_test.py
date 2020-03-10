import unittest
from notification_utils.ding_talk import DingTalk

class NotificationTest(unittest.TestCase):

    def test_ding_talk(self):
        ding_talk = DingTalk('0e960f1b44ed6e5f7cb5874e709cc24d6c37827de9a63ba1b18403f0a47ea87d')
        success = ding_talk.send_message('13521797236','Warning','SEC047fd6938eec907fdbefa2120639a9a178d1ff769a674c4027e7d41f2ea3dd13')
        print(success)


if __name__ == '__main__':
    unittest.main()
