import unittest
from server.helpers.user_helper import user_helper
from server.dal.user_provider import user_provider
from server.mysql_dal.mysql_user_provider import mysql_user_provider
from server.common.my_user import User
from mock import patch


class UserTest(unittest.TestCase):
    user_provider_new = user_provider()
    mysql_user_provider_new = mysql_user_provider()
    new_user_helper = user_helper(mysql_user_provider_new)

    def test_user_with_negative_id(self):
        self.assertNotIsInstance(self.new_user_helper.get_user_by_id('-1'), User)

    def test_user_with_zero_id(self):
        self.assertNotIsInstance(self.new_user_helper.get_user_by_id('0'), User)

    # @patch('user_helper.user_provider.select_user', returnValue=(2, 1, 'My name is Dor', 'https://instagram.fsdv1-1.fna.fbcdn.net/t51.2885-15/e35/13707273_1750406611904169_1663722252_n.jpg?ig_cache_key=MTI5NTA0MzAwODY0MzEwNDIwNw%3D%3D.2'))
    def test_user_with_int_id(self):
        self.assertIsInstance(self.new_user_helper.get_user_by_id(int(1)), User)

    def test_user_with_valid_id(self):
        self.assertIsInstance(self.new_user_helper.get_user_by_id('1'), User)

if __name__ == '__main__':
    unittest.main()