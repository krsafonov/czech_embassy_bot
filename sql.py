from mysql.connector import connect, Error
import logging
from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE


def insert_user(uname, uid, extra=""):
    this_user_already_exists = False
    if not get_all_users() is None:
        for user in get_all_users():
            if uid in user:
                this_user_already_exists = True
    if not this_user_already_exists:
        insert_ratings_query = """
        INSERT INTO tg_users
        (uname, uid, extra)
        VALUES (%s, %s, %s)
        """
        try:
            with connect(
                    host=SQL_HOST,
                    user=SQL_USER,
                    password=SQL_PASSWORD,
                    database=SQL_DATABASE
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(insert_ratings_query, (uname, uid, extra))
                    connection.commit()
                    return True
        except Error as e:
            print(e)
        return False


def get_all_users():
    try:
        with connect(
                host=SQL_HOST,
                user=SQL_USER,
                password=SQL_PASSWORD,
                database=SQL_DATABASE
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * from tg_users")
                return cursor.fetchall()
    except Error as e:
        print(e)
