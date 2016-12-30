from server.common.my_user import User
import logging

# create logger
logging.basicConfig(filename='logs.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class user_helper(object):
    def __init__(self, user_provider):
        self.user_provider = user_provider
        self.logger = logging.getLogger(__name__)


    def is_user_exist(self, user_id):
        # calling the implematation of the provider from the init
        result = self.user_provider.select_user(user_id)
        if result is None:
            return False
        else:
            return True

    def is_user_public(self, user_id):
        result = self.user_provider.select_user(user_id)
        if result["public"] is False:
            return False
        else:
            return True

    # def get_user_by_id(self, user_id):
    #     user_details = []
    #     result = self.user_provider.select_user(user_id)
    #     #insert to user_deatils list all the data insted of a tuple
    #     user_details = list(result)
    #     user_object = User(*user_details)
    #     return user_object


    def get_user_by_id(self, user_id):
        user_details = []
        try:
            result = self.user_provider.select_user(user_id)
            if result is None:
                raise ValueError
            # insert to user_deatils list all the data insted of a tuple
            else:
                user_details = list(result)
                user_object = User(*user_details)
                return user_object
        except ValueError:
            self.logger.error('This is unvalid user_id')
