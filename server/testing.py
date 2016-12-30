import mysql.connector


# #THE CONNECTION DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
# server_host = 'localhost'
# user = 'root'
# password = '8717003'
# database = 'my_instagram'
#
# #VALUE NEED TO BE FILE_PATH
# class mysql_user_provider(user_provider):
#     def select_user(self, user_id):
#         #repalce all in that
#         conn = mysql.connector.connect(user = user,password = password,host = server_host ,database = database)
#         cursor = conn.cursor()
#         sql = """SELECT * FROM user WHERE user_id = %s""" %(user_id)
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         conn.close()
#         return result
#
# one_test_class = user_provider()
# test_class = mysql_user_provider()
# print(test_class.select_user('1'))
from mysql_dal.mysql_user_provider import mysql_user_provider
from dal.user_provider import user_provider
from common.my_user import User


class user_helper(object):
    def __init__(self, user_provider):
        self.user_provider = user_provider

    def get_user_by_id(self, user_id):
        user_details = []
        try:
            result = self.user_provider.select_user(user_id)
            if result is None:
                raise ValueError
            # insert to user_deatils list all the data insted of a tuple
            else:
                user_details = list(result)
                user_object = User(*user_details)
                return user_object
        except ValueError:
            self.logger.error('This is unvalid user_id')


user_provider_new = user_provider()
mysql_user_provider_new = mysql_user_provider()
new_user_helper = user_helper(mysql_user_provider_new)
print(new_user_helper.get_user_by_id('1'))