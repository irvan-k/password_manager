import subprocess
from password_hash import get_password, get_random_password,copy2clip
from database import store_passwords


def menu():
    print('- ' * 30)
    print(('- ' * 13) + 'Menu ' + ('-' * 13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('q. Exit')
    print('-' * 30)
    return input(': ')


def create():
    print('Please proivide the name of the site or app you want to generate a password for')
    app_name = input()
    passw = get_random_password()
    copy2clip(passw)
    print('-' * 30)
    print('')
    print('Your password has now been created and copied to your clipboard')
    print('')
    print('-' * 30)
    user_email = input('Please provide a user email for this app or site: \n')
    username = input('Please provide a username for this app or site (if applicable): ')
    if username == None:
        username = ''
    url = input('Please paste the url to the site that you are creating the password for: ')
    store_passwords(passw, user_email, username, url, app_name)
