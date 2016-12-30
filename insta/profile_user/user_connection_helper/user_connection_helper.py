# from dal.user_connection_provider import user_connection_provider
# from profile_user.models import InstaUser
from .mysql_user_connection_provider import select_user_connection_followers_count, select_user_connection_following_count

def get_user_followings_count(user_id):
    following_count_tuple = select_user_connection_following_count(user_id)
    #result is a tuple , so this map take it into a int
    counter = int(following_count_tuple[0])
    return counter

# return a list of users object that an user_id followed them

# def get_user_followings(self, user_id):
#     following_id_list = []
#     user_deatils_list=[]
#     following_user_object_list = []
#     user_id_tuple = mysql_user_connection_provider.select_user_connection_following(user_id)
#     # result is a tuple , so this map take it into a list
#     map((lambda x: following_id_list.append(x[0])), user_id_tuple)
#     # retriving user object list for every user id in following_id_list
#     for following_user_id in following_id_list:
#         # retriving a tuple of the deatils of the user_id
#         user_deatils_tuple = mysql_user_connection_provider.select_user(following_user_id)
#         # making the tuple to a list so we can make an object out of him
#         map((lambda x: user_deatils_list.append(x)), user_deatils_tuple)
#         # making a list that conatine users_object
#         following_user_object_list.append(InstaUser(*user_deatils_list))
#     return following_user_object_list


def get_user_followers_count(user_id):
    followers_count_tuple = select_user_connection_followers_count(user_id)
    # result is a tuple , so this map take it into a int
    counter = int(followers_count_tuple[0])
    return counter

# #return a list of users object that following an user_id
# def get_user_followers(self, user_id):
#     followers_id_list = []
#     user_deatils_list = []
#     followers_user_object_list = []
#     user_id_tuple = mysql_user_connection_provider.select_user_connection_followers(user_id)
#     # result is a tuple , so this map take it into a list
#     map((lambda x: followers_id_list.append(x[0])), user_id_tuple)
#     # retriving user object list for every user id in followers_id_list
#     for followers_user_id in followers_id_list:
#         # retriving a tuple of the deatils of the user_id
#         user_deatils_tuple = self.user_provider.select_user(followers_user_id)
#         # making the tuple to a list so we can make an object out of him
#         map((lambda x: user_deatils_list.append(x)), user_deatils_tuple)
#         # making a list that conatine users_object
#         followers_user_object_list.append(InstaUser(*user_deatils_list))
#     return followers_user_object_list

