import mysql.connector
from server.dal.post_provider import post_provider

#THE CONNECTION DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
server_host = 'localhost'
user = 'root'
password = 'adiavital8717003'
database = 'insta'

#VALUE NEED TO BE FILE_PATH
class mysql_post_provider(post_provider):

    def insert_post(self, user_id, id, date, value, description):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """INSERT INTO profile_user_post(user_id, id, date, value, description) VALUES ( '%s', '%s', '%s'  ,'%s', LOAD_FILE('%s'), '%s')"""%(user_id, id, date, value, description)
        try:
            # in the second brekets there are the param to the sql query
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def delete_post(self, id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """DELETE FROM profile_user_post WHERE id = '%s'""" %(id)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def update_post(self, id ,description):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """UPDATE profile_user_post SET description = %s WHERE id = %s""" %(description, id)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    def select_post_by_id(self, id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_post WHERE id = %s""" %(id)
        cursor.execute(sql)
        results = cursor.fetchone()
        conn.close()
        return results

    def select_post_by_user_id(self, user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_post WHERE user_id = %s""" %(user_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results

    def select_post_count_by_user(self, user_id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT count(*) FROM profile_user_post WHERE user_id = %s""" %(user_id)
        cursor.execute(sql)
        results = cursor.fetchone()
        conn.close()
        return results


    def coloumes_name(self, id):
        conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
        cursor = conn.cursor()
        sql = """SELECT * FROM profile_user_post WHERE id = %s""" %(id)
        cursor.execute(sql)
        column_names = cursor.column_names
        return column_names


