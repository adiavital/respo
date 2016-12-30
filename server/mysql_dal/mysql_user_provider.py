import mysql.connector
from server.dal.user_provider import user_provider


#THE CONNECTION DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
server_host = 'localhost'
user = 'root'
password = 'adiavital8717003'
database = 'insta'


# VALUE NEED TO BE FILE_PATH
class mysql_user_provider(user_provider):

    def insert_user(self, user_id, public, description , profile_picture):
        conn = mysql.connector.connect(user=user ,password=password, host=server_host , database=database)
        cursor = conn.cursor()
        sql = """INSERT INTO profile_user_instauser(user_id, public, description , profile_picture) VALUES ( '%s', '%s', '%s', '%s')"""  %('user_id', 'public', 'description', 'profile_picture')
        try:
            # in the second brekets there are the param to the sql query
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def delete_user(self, user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """DELETE FROM profile_user_instauser WHERE post_id = '%s'""" %(user_id)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def update_user_public(self, user_id, public):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """UPDATE profile_user_instauser SET public = %s WHERE user_id = %s""" %(user_id, public)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def update_user_description(self, user_id, description):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """UPDATE profile_user_instauser SET description = %s WHERE user_id = %s""" %(user_id, description)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def update_user_profile_picture(self, user_id, profile_picture):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """UPDATE profile_user_instauser SET profile_picture = %s WHERE user_id = %s""" %(user_id, profile_picture)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def select_user(self, user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_instauser WHERE user_id = %s""" %(user_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.close()
        return result

    def coloumes_name(self ,user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_instauser WHERE user_id = %s""" %(user_id)
        cursor.execute(sql)
        column_names = cursor.column_names
        return column_names

