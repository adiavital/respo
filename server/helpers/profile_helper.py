from server.helpers.post_helper import post_helper
from server.helpers.user_helper import user_helper
from server.helpers.profile_post_helper import profile_post_helper
from server.helpers.user_connection_helper import user_connection_helper
from server.models.my_profile import Profile
import logging
import os
import inspect

logging.basicConfig(filename='logs.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class profile_helper(object):
    # with which implementation of dal the helper will work
    def __init__(self, user_provider, post_provider , user_connection_provider , like_provider , comment_provider):
        self.user_provider = user_provider
        self.post_provider = post_provider
        self.user_connection_provider = user_connection_provider
        self.like_provider = like_provider
        self.comment_provider = comment_provider
        # create logger
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
            self.logger.error('In This path: %s ,in this func %s pop this log: unvalid user_id' % (
            os.path.abspath(__file__), inspect.stack()[0][3]))

    def get_user_connection(self, user_id ):
        user_connection_local_helper = user_connection_helper(self.user_connection_provider, self.user_provider)
        followers_count = user_connection_local_helper.get_user_followers_count(user_id)
        following_count = user_connection_local_helper.get_user_followings_count(user_id)
        return followers_count, following_count

    def get_user_profile_posts(self, user_id):
        profile_posts_list = []
        local_post_helper = post_helper(self.post_provider)
        local_profile_post_helper = profile_post_helper(self.post_provider, self.like_provider, self.comment_provider)
        user_posts = local_post_helper.get_user_posts(user_id)
        # take every post in the user post list ,
        #  take its post id and creating profile_post object , finally put it in a list
        for post in user_posts:
            profile_posts_list.append(local_profile_post_helper.get_profile_post_object(post.post_id))
        return profile_posts_list

    @classmethod
    def get_profile(cls, user_id):
        logger = logging.getLogger(__name__)
        profile_help_list = []
        try:
            valid_user = cls.get_user(user_id)
            if valid_user == None:
                raise ValueError
            else:
                profile_help_list.append(cls.get_user(user_id))
                profile_help_list.append(cls.get_user_connection(user_id))
                profile_help_list.append(cls.get_user_profile_posts(user_id))
                profile_object = Profile(*profile_help_list)
                return profile_object
        except ValueError:
            logger.error('In This path: %s ,in this func %s pop this log: unvalid user_id' % (os.path.abspath(__file__), inspect.stack()[0][3]))






# def get_user(self , user_id):
#     local_user_helper = user_helper(self.user_provider)
#     # i nedd to write expation
#     if local_user_helper.is_user_exist(user_id) == False:
#         return False
#     else:
#         user_object = local_user_helper.get_user_by_id(user_id)
#         return user_object.user_id, user_object.user_name, user_object.description, user_object.profile_picture, user_object.public
