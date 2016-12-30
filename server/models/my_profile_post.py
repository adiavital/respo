
class ProfilePost(object):

    def __init__(self, post_id, date, value, description, likes, comments):
        self.post_id = post_id
        self.date = date
        self.value = value
        self.description = description
        self.likes = likes
        self.comments = comments

        #likes and comments are lists

