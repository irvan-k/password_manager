import psycopg2
import bcrypt


# store password in db
def store_passwords(password, email, username, url, app_name):
    try:
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        insert_query = """ INSERT INTO account (password,email,username,url,app_name) VALUES ( %s, %s, %s, %s, %s)"""
        record_to_insert = (password, email, username, url, app_name)
        cursor.execute(insert_query, record_to_insert)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def find_password(app_name):
    try:
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        postgres_select_query = """ SELECT password FROM account WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        conn.commit()
        result = cursor.fetchone()
        print('Password is: ')
        print(result[0])

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        postgres_select_query = """ SELECT * FROM account WHERE email = '""" + user_email + "'"
        cursor.execute(postgres_select_query, user_email)
        conn.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row) - 1):
                print(data[i] + row[i])
        print('')
        print('-' * 30)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


# this is set password master in database for first time with id 1 only

def master_password_first(master_hashed_password):
    try:
        master_hex_password = master_hashed_password.decode("utf-8")
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        insert_query = """ INSERT INTO master_password (id,master_password) VALUES (%s, %s)"""
        record_to_insert = ("1", master_hex_password)
        cursor.execute(insert_query, record_to_insert)
        conn.commit()
        print("master_password set for the first time")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


# this is for checking entered password and master password in db
def master_password_check(user_password):
    try:
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        req_query = "SELECT master_password from master_password where id = 1"
        cursor.execute(req_query)
        result = cursor.fetchone()
        master_password = result[0].encode('utf-8')
        if bcrypt.checkpw(user_password, master_password):
            return True
        else:
            return False




    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
