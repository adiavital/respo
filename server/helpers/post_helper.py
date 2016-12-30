from server.common.my_post import Post
import logging
import os
import inspect

# create logger
logging.basicConfig(filename='logs.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class post_helper(object):
    def __init__(self, post_provider):
        self.post_provider = post_provider
        self.logger = logging.getLogger(__name__)


    # Return a list of object that present the posts of the user_id

    def get_user_posts(self, user_id):
        post_list = []
        post_object_list = []
        posts_tuple = self.post_provider.select_post_by_user_id(user_id)
        # making the tuple of tuples to a list of lists (each list is a post)
        post_list = map(lambda one_post: post_list.append(list(one_post)), posts_tuple)
        for post in post_list:
            post_object = Post(*post)
            post_object_list.append(post_object)
        return post_object_list

    def get_user_num_of_posts(self, user_id):
        post_count_tuple = self.post_provider.select_post_count_by_user(user_id)
        #result is a tuple , so this map take it into a int
        counter = int(post_count_tuple[0])
        return counter

    def get_post_deatil_list(self, post_id):
        try:
            post = self.post_provider.select_post_by_id(post_id)
            if post is None:
                raise ValueError
            else:
                # insert to user_deatils list all the data insted of a tuple
                post_details = list(post)
                return post_details
        except ValueError:
            self.logger.error('In This path: %s ,in this func %s pop this log: unvalid user_id' % (
            os.path.abspath(__file__), inspect.stack()[0][3]))

    def get_post_object(self, post_id):
        post = self.post_provider.select_post_by_post_id(post_id)
        # insert to user_deatils list all the data insted of a tuple
        post_details = list(post)
        post_object = Post(*post_details)
        return post_object


