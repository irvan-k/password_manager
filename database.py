import psycopg2
import bcrypt


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
