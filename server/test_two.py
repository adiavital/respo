from helpers.post_helper import post_helper
from helpers.user_helper import user_helper
from helpers.user_connection_helper import user_connection_helper
from dal.user_provider import user_provider
from mysql_dal.mysql_user_provider import mysql_user_provider


class profile_helper(object):
    def __init__(self, user_provider):
        self.user_provider = user_provider

    def get_user(self, user_provider, user_id):
        my_local_user_helper = user_helper(user_provider)
        result = my_local_user_helper.is_user_exist(user_id)
        return result

user_provider_new = user_provider()
mysql_user_provider_new = mysql_user_provider()
new_profile_helper = profile_helper(mysql_user_provider_new)
print(new_profile_helper.get_user(mysql_user_provider_new,1))
