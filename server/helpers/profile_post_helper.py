from server.helpers.post_helper import post_helper
from server.helpers.like_helper import like_helper
from server.helpers.comment_helper import comment_helper
from server.models.my_profile_post import ProfilePost
import logging
import os
import inspect

# create logger
logging.basicConfig(filename='logs.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class profile_post_helper(object):
    def __init__(self, post_provider, like_provider, comment_provider):
        self.post_provider = post_provider
        self.like_provider = like_provider
        self.comment_provider = comment_provider
        self.logger = logging.getLogger(__name__)


    def get_profile_post_object(self, post_id):
        my_local_post_helper = post_helper(self.post_provider)
        my_local_like_helper = like_helper(self.like_provider)
        my_local_comment_helper = comment_helper(self.comment_provider)
        try:
            # get a list that present a post object
            post_deatil_list = my_local_post_helper.get_post_deatil_list(post_id)
            if post_deatil_list is None:
                raise ValueError
            else:
                # append a list of likes objects
                post_deatil_list.append(my_local_like_helper.get_post_likes(post_id))
                # append a list of comments objects
                post_deatil_list.append(my_local_comment_helper.get_post_comments(post_id))
                profile_post_object = ProfilePost(*post_deatil_list)
                return profile_post_object
        except ValueError:
            self.logger.error('In This path: %s ,in this func %s pop this log: unvalid user_id' % (os.path.abspath(__file__), inspect.stack()[0][3]))

