class User(object):
    def __init__(self, user_id, user_name, join_date, public, description, profile_picture):
        self.user_id = user_id
        self.user_name = user_name
        self.join_date = join_date
        self.public = public
        self.description = description
        self.profile_picture = profile_picture

    def __str__(self):
        return self.user_name + ' with id of: ' + str(self.user_id)

    # def new_user(user_id, user_name, join_date, public, description, profile_picture):
    #     user = User(user_id, user_name, join_date, public, description , profile_picture)
    #     return user