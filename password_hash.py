from re import match

import bcrypt
import getpass


# def query_master_pwd(hashed_master_password):
#     if bcrypt.checkpw(hashed_master_password, ):
#         print("it is match")
#     else:
#         print("it dosent match")
#
#
#



password = getpass.getpass('Password:')
byte_password = bytes(password, encoding='utf8')
hashed = bcrypt.hashpw(byte_password, bcrypt.gensalt())

    # return hashed



# print(hashed_password)
# if bcrypt.checkpw(byte_password, hashed):
#     print("it is match")
# else:
#     print("it dosent match")
