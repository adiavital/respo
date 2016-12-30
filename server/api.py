from helpers import profile_helper


# root url: api.adistagram.com
class api():

    # /profile/user_id
    def get_user_profile(self, userid):

        # return profile model
        profile = profile_helper.get_profile(userid)
        return profile

