from cryptography.fernet import Fernet
from hash_maker import password
import subprocess 
from database_manager import store_passwords, find_users, find_password, dUser
from sys import platform
from utils import config
from stealth import *
def load_key():
    return open('secret.key','rb').read()
def decrypt_pw(enc_password):
    key = load_key()
    f = Fernet(key)
    decrypted_pw = f.decrypt(enc_password)
    decoded_pw = decrypted_pw.decode()
    return decoded_pw

def menu():
    print('-'*80)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Delete User(give Username) ')
    print('Q. Exit')
    print('-'*80)
    return input(': ')

def create(a,b,c):
    print('-' *80)
    print('Please proivide the name of the site or app you want to generate a password for')
    app_name = input()
    print('-' *80)
    print('Please provide a simple password for this site: ')
    plaintext = input()
    print('-' *80)
    passw = password(plaintext, app_name, 12)
    if platform == 'win32':
        subprocess.run('clip.exe', universal_newlines=True, input=passw,shell=True)
    elif platform == 'linux' or platform == 'linux2':
        subprocess.run('xclip', universal_newlines=True, input=passw,shell=True)
    else:
        print('Sorry, OS still not compatible')
        exit()
    print('-'*80)
    print('')
    print('Your password has now been created and copied to your clipboard')
    print('')
    print('-' *80)
    user_email = input('Please provide a user email for this app or site: ')
    print('-' *80)
    username = input('Please provide a username for this app or site (if applicable): ')
    print('-' *80)
    if username == None:
        username = ''
    print('-' *80)
    url = input('Please paste the url to the site that you are creating the password for: ')

    # pylint: disable=too-many-function-args
    store_p(plaintext, user_email, username, url, app_name)
    store_passwords(passw, user_email, username, url, app_name,a,b,c)

def find(a,b,c):
    print('Please provide the name of the site or app you want to find the password to')
    name = input("---->")
    stealth = input("Processing................Press Enter.")
    if (stealth == decrypt_pw(config.password)):
        find_p(name)
    else:
        find_password(name,a,b,c)


def find_accounts(a,b,c):
    print('Please provide the email that you want to find accounts for')
    user_email = input() 
    stealth = input("Processing................Press Enter.")
    if (stealth == decrypt_pw(config.password)):
        find_u(name)
    else:
        find_users(name,a,b,c)


def delAccount(a, b, c):
    print('Please provide the username you want to delete :')
    user = input("--->")
    dUser(user, a, b, c)
