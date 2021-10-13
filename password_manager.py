import getpass

import bcrypt

from menu import menu, create, find, find_accounts


# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

# passw = getpass.getpass('Enter master password:')
# byte_password = bytes(passw, encoding='utf8')
# hashed_master_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())



if passw == secret:
    print('You\'re in')

else:
    print('no luck')
    exit()

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
