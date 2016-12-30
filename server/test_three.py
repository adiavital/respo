# from mysql_dal.mysql_user_provider import mysql_user_provider
# from common.my_user import User
#
# new_mysql_user_provider = mysql_user_provider()
#
# user_id = 1
# user_details = []
# result = new_mysql_user_provider.select_user(user_id)
# # insert to user_deatils list all the data from each coloum of the user row
# # for coulum in new_mysql_user_provider.coloumes_name(user_id):
# #     user_details.append(result[str(coulum)])
# user_details = list(result)
# print user_details
# user_object = User(*user_details)
# print user_object
# print user_object.user_id
#
#
from dal.user_provider import user_provider
from mysql_dal.mysql_user_provider import mysql_user_provider
from helpers.user_helper import user_helper
import logging
import os
import inspect

logging.basicConfig(filename='logs.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class profile_helper(object):
    def __init__(self, user_provider):
        self.user_provider = user_provider
        self.logger = logging.getLogger(__name__)

    def get_user(self, user_id):
        local_user_helper = user_helper(self.user_provider)
        try:
            local_user_helper.is_user_exist(user_id)
            if local_user_helper.is_user_exist(user_id) == False:
                raise ValueError
            else:
                user_object = local_user_helper.get_user_by_id(user_id)
                return user_object.user_id, user_object.user_name, user_object.description, user_object.profile_picture, user_object.public
        except ValueError:
            self.logger.error('In This path %s ,in this func %s , unvalid user_id' %(os.path.abspath(__file__), inspect.stack()[0][3]))

user_provider_new = user_provider()
mysql_user_provider_new = mysql_user_provider()
new_profile_helper = profile_helper(mysql_user_provider_new)
print(new_profile_helper.get_user('1'))

