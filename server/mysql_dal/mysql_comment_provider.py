import mysql.connector
from server.dal.comment_provider import comment_provider

#THE activity DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
server_host = 'localhost'
user = 'root'
password = 'adiavital8717003'
database = 'insta'


class mysql_comment_provider(comment_provider):
    def insert_comment(self, id, post_id , user_id, comment_value):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        #ACTIVITY ID IS AUTOMOTIC INCRICMENT 
        sql = """INSERT INTO profile_user_comment(id, post_id , user_id, comment_value) VALUES ( '%s', '%s' ,'%s', '%s')""" %(comment_id, post_id , user_id, comment_value)
        try:
            # in the second brekets there are the param to the sql query
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def delete_comment(self, id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """DELETE FROM profile_user_comment WHERE id='%s'""" %(id)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()



    def select_comment_by_post(self, post_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_comment WHERE post_id = %s""" %(post_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results

