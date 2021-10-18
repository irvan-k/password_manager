from re import match

import bcrypt
import getpass


def get_password():
    password = getpass.getpass('Please enter your master password: ')
    encoded = password.encode('utf-8')
    return encoded


# make hash password and return
def make_hash():
    password = getpass.getpass('Please enter your master password for first time: ')
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
