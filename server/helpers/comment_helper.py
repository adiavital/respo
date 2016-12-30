from server.common.my_comment import Comment

class comment_helper(object):
    def __init__(self, comment_provider):
        self.comment_provider = comment_provider

    def get_post_comments(self, post_id):
        comments_object_list = []
        comments_list = []
        comments_tuple = self.comment_provider.select_comment_by_post(post_id)
        # making the tuple of tuples to a list of lists (each list is a comment)
        for one_comment in comments_tuple: comments_list.append(list(one_comment))
        for comment in comments_list:
            #making a comment object out of a comment mini list
            comment_object = Comment(*comment)
            comments_object_list.append(comment_object)
        return comments_object_list
