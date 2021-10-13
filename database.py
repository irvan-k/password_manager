import psycopg2
from psycopg2 import Error


# this is just test for insert_query to db
def test_insert():
    try:
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        insert_query = """ INSERT INTO account (password,email,username,url,app_name) VALUES ( 'jackpass', 'jack@email.com','jack','https://jack.com','jackmail')"""
        cursor.execute(insert_query)
        conn.commit()
        print("1 Record inserted successfully")
        cursor.execute("SELECT * from account")
        print("Result ", cursor.fetchall())

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


# test_insert()


# trying to connect to database and make cursor and excute
def connect():
    try:
        conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                                database="password_manager")
        cursor = conn.cursor()
        print("PostgreSQL server information")
        print(conn.get_dsn_parameters(), "\n")
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
