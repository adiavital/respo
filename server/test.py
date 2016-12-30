# import MySQLdb
#
# from dal.post_provider import post_provider
# from common.my_post import Post
# from dal.user_connection_provider import user_connection_provider
#
# #THE CONNECTION DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
# server_host = 'localhost'
# user = 'root'
# password = '8717003'
# database = 'my_instagram'

# class mysql__user_connection_provider(user_connection_provider):
#     def select_user_connection_followers(self, user_id):
#         conn = MySQLdb.connect(server_host, user, password, database)
#         cursor = conn.cursor()
#         sql = """SELECT followed_id FROM user_connection WHERE user_id = %s"""
#         cursor.execute(sql, (user_id))
#         results = cursor.fetchall()
#         conn.close()
#         return results
#         # print results
#
# user_connection_provider_new = user_connection_provider()
# mysql__user_connection_provider_new = mysql__user_connection_provider()
# # mysql__user_connection_provider_new.select_user_connection_followers('1')
# result = mysql__user_connection_provider_new.select_user_connection_followers('1')
#
# list_two=[]
# map((lambda x : list_two.append(x[0])), result)
# print(list_two)

# --------------------

# class mysql_user_provider(user_provider):
#     def select_user(self, user_id):
#         conn = MySQLdb.connect(server_host, user, password, database)
#         cursor = conn.cursor()
#         sql = """SELECT * FROM user WHERE user_id = %s"""
#         cursor.execute(sql, user_id)
#         result = cursor.fetchone()
#         conn.close()
#         return result
#
# user_provider_new = user_provider()
# mysql_user_provider_new = mysql_user_provider()
# # mysql__user_connection_provider_new.select_user_connection_followers('1')
# result = mysql_user_provider_new.select_user('1')
#
# list_two=[]
# map((lambda x : list_two.append(x)), result)
# print(list_two)
# my_user = User(*list_two)
# print(my_user)
#
# ---------------

# class mysql_user_provider(user_provider):
#     def select_user_connection_following_count(self, user_id):
#         conn = MySQLdb.connect(server_host, user, password, database)
#         cursor = conn.cursor()
#         sql = """SELECT following_count FROM user_connection_count WHERE user_id = %s"""
#         cursor.execute(sql, (user_id))
#         results = cursor.fetchone()
#         conn.close()
#         return results
#
# user_provider_new = user_provider()
# mysql_user_provider_new = mysql_user_provider()
# result = mysql_user_provider_new.select_user_connection_following_count('1')
# #
# list_two=[]
# counter=int(result[0])
# print counter

# -----------

# class mysql_post_provider(post_provider):
#     def select_post_by_user_id(self, user_id):
#         conn = MySQLdb.connect(server_host, user, password, database)
#         cursor = conn.cursor()
#         sql = """SELECT * FROM post WHERE user_id = %s"""
#         cursor.execute(sql, (user_id))
#         results = cursor.fetchall()
#         conn.close()
#         return results
#
# post_provider_new = post_provider()
# mysql_post_provider_new = mysql_post_provider()
# result = mysql_post_provider_new.select_post_by_user_id('1')
# #
# print result
# list_two=[]
# map(lambda x : list_two.append(list(x)), result)
# print list_two
# for x in list_two:
#     my_post = Post(*x)
#     print my_post


#--------------------------
#
# from mysql_dal.mysql_user_provider import mysql_user_provider
# from dal.user_provider import user_provider
#
# new_user_provider = user_provider()
# new_mysql_user_provider = mysql_user_provider()
#
# result = new_mysql_user_provider.select_user(user_id='2')
# print(result)

#-------------------------
from mysql_dal.mysql_post_provider import mysql_post_provider
from dal.post_provider import post_provider
from helpers.post_helper import post_helper

post_provider_new = post_provider()
mysql_post_provider_new = mysql_post_provider()
post_helper_new = post_helper(mysql_post_provider_new)

result = post_helper_new.get_post_deatil_list(post_id='2')
print(result)