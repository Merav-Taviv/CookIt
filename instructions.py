'''
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
'''
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def add_new_user(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = "INSERT INTO tbl_users(userId, userName, userPassword, userMail )VALUES('8', 'Dvori', '123789', 'shirayt1oo@gmail.com')"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tbl_users WHERE userId=8'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def main():
    database = r"C:\Users\מירב\PycharmProjects\pythonProject\Cook_It.db"
    conn = create_connection(database)
    with conn:
        # add_new_user(conn)
        delete_task(conn, 8)






if __name__ == '__main__':
    main()


