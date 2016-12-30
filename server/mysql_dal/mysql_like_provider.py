import mysql.connector
from server.dal.like_provider import like_provider

#THE activity DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
server_host = 'localhost'
user = 'root'
password = 'adiavital8717003'
database = 'insta'


class mysql_like_provider(like_provider):
    def insert_like(self, post_id, user_id ):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        #ACTIVITY ID IS AUTOMOTIC INCRICMENT 
        sql = """INSERT INTO profile_user_like(post_id, user_id ) VALUES ( '%s', '%s')""" %(post_id, user_id)
        try:
            # in the second brekets there are the param to the sql query
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()


    def delete_like(self, post_id , user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """DELETE FROM profile_user_like WHERE post_id = '%s' AND user_id='%s'""" %(post_id , user_id)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()


    def select_like_by_user(self, user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_like WHERE user_id = %s""" %(user_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results


    def select_like_by_post(self, post_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_like WHERE post_id = %s""" %(post_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results


