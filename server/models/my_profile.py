class Profile(object):

    def __init__(self, user_id, user_name, description, profile_picture, public , followers_count, following_count ,posts):
        self.user_id = user_id
        self.user_name = user_name
        self.description = description
        self.profile_picture = profile_picture
        self.public =public
        self.followers_count = followers_count
        self.following_count = following_count
        self.posts = posts

