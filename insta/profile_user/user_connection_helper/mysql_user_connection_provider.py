import mysql.connector
from .user_connection_provider import user_connection_provider

#THE CONNECTION DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
server_host = 'localhost'
user = 'root'
password = 'adiavital8717003'
database = 'insta'


def insert_user_connection(user_id, followed_user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """INSERT INTO profile_user_userconnection(user_id, followed_user_id) VALUES ( '%s', '%s' )""" %(user_id, followed_user_id)
    try:
        # in the second brekets there are the param to the sql query
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def delete_user_connection(user_id, followed_user_id ):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """DELETE FROM profile_user_userconnection WHERE user_id = '%s' AND followed_user_id='%s'""" %(user_id, followed_user_id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

#NO NEED OF UPDATE IN THIS TABLE

#get the usrers that this id followd them
def select_user_connection_following(followed_user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """SELECT user_id FROM profile_user_userconnection WHERE followed_user_id = %s""" %(followed_user_id)
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results

#get the users that are followers of this id

def select_user_connection_followers(user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """SELECT followed_user_id FROM profile_user_userconnection WHERE user_id = %s""" %(user_id)
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results

def select_user_connection_following_count(user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """SELECT following_count FROM user_connection_count WHERE user_id = %s""" %(user_id)
    cursor.execute(sql)
    results = cursor.fetchone()
    conn.close()
    return results

def select_user_connection_followers_count(user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """SELECT followers_count FROM user_connection_count WHERE user_id = %s""" %(user_id)
    cursor.execute(sql)
    results = cursor.fetchone()
    conn.close()
    return results