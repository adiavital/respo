from server.common.my_like import Like

class like_helper(object):
    def __init__(self, like_provider):
        self.like_provider = like_provider

    def get_post_likes(self ,post_id):
        likes_object_list = []
        likes_list = []
        likes_tuple = self.like_provider.select_like_by_post(post_id)
        # making the tuple of tuples to a list of lists (each list is a like)
        for one_like in likes_tuple: likes_list.append(list(one_like))
        for like in likes_list:
            #making a like object out of a like mini list
            like_object = Like(*like)
            likes_object_list.append(like_object)
        return likes_object_list
