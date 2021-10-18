import psycopg2
from database import master_password_first, master_password_check
from password_hash import make_hash, get_password

# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

# passw = getpass.getpass('Enter master password:')
# byte_password = bytes(passw, encoding='utf8')
# hashed_master_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())

try:
    conn = psycopg2.connect(user="postgres", password="7092", host="localhost", port="5432",
                            database="password_manager")
    cursor = conn.cursor()
    query = "SELECT id FROM master_password WHERE EXISTS(SELECT * from account)"
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Hello\n welcome this is your first time using Mypm by irvan enjoy :) ")
        hashed = make_hash()
        master_password_first(hashed)
        pass
    else:
        user_pass = get_password()
        if master_password_check(user_pass):
            print("Welcome")
        else:
            print("Sorry wrong password")
            exit()




except(Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

#
#
# if passw == secret:
#     print('You\'re in')
#
# else:
#     print('no luck')
#     exit()
#
# choice = menu()
# while choice != 'Q':
#     if choice == '1':
#         create()
#     if choice == '2':
#         find_accounts()
#     if choice == '3':
#         find()
#     else:
#         choice = menu()
# exit()
