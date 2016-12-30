import unittest
from server.helpers.profile_post_helper import profile_post_helper
from server.dal.post_provider import post_provider
from server.dal.comment_provider import comment_provider
from server.dal.like_provider import like_provider
from server.mysql_dal.mysql_post_provider import mysql_post_provider
from server.mysql_dal.mysql_like_provider import mysql_like_provider
from server.mysql_dal.mysql_comment_provider import mysql_comment_provider
from server.models.my_profile_post import Profile_post
from mock import patch


class ProfilePostrTest(unittest.TestCase):
    post_provider_new = post_provider()
    mysql_post_provider_new = mysql_post_provider()

    like_provider_new = like_provider()
    mysql_like_provider_new = mysql_like_provider()

    comment_provider_new = comment_provider()
    mysql_comment_provider_new = mysql_comment_provider()

    new_profile_post_helper = profile_post_helper(mysql_post_provider_new,
                                                  mysql_like_provider_new,
                                                  mysql_comment_provider_new)

    def test_profile_post_with_negative_id(self):
        self.assertNotIsInstance(self.new_profile_post_helper.get_profile_post_object('-1'), Profile_post)

    @patch('new_profile_post_helper.post_helper.get_post_deatil_list', returnValue="[2, datetime.date(2016, 12, 24), 'https://instagram.fsdv1-1.fna.fbcdn.net/t51.2885-15/e35/14719538_1149540088458732_517405407249956864', 'wow', 2]")
    def test_profile_post_with_valid_id(self):
        self.assertIsInstance(self.new_profile_post_helper.get_profile_post_object('1'), Profile_post)


if __name__ == '__main__':
    unittest.main()