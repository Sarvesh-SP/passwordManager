#importing configs and credentials
from utils import config
from update import update
#from secret import get_secret_key
from menu import menu, create, find, find_accounts, delAccount
#importing the crypto module
from cryptography.fernet import Fernet

#functions to generate\load an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key','wb') as key_file:
        key_file.write(key)
def load_key():
    return open('secret.key','rb').read()

#functions to encrytpt and decrypt the password
def encrypt_pw(password):
    key = load_key()
    encoded_pw = password.encode()
    f = Fernet(key)
    encrypted_pw = f.encrypt(encoded_pw)
    return encrypted_pw
def decrypt_pw(enc_password):
    key = load_key()
    f = Fernet(key)
    decrypted_pw = f.decrypt(enc_password)
    decoded_pw = decrypted_pw.decode()
    return decoded_pw



#this function is run to see whether the programm has already been run and parse data from the config_file.txt file
def launch():
    global launched
    launched = False
    if launched == config.islaunched:
        generate_key()
        global user_name,password,user,pw_db,dbname
        print("---------------------------------------------------------")
        print('Please Enter the masterUsername: ')
        user_name = input('--> ')
        print("---------------------------------------------------------")
        password = encrypt_pw(input('Enter your password: \n--> '))
        print("---------------------------------------------------------")
        print('Enter the name of the user of your data base: ')
        user = input('--> ')
        print("---------------------------------------------------------")
        print('The password of the data base: ')
        pw_db = input('--> ')
        print("---------------------------------------------------------")
        print('Finally, the name of the data base: ')
        dbname = input('--> ')
        print("---------------------------------------------------------")
        launched = True
        args = ["islaunched","user_name","password","dbuser","dbname","dbpw"]
        credentials = [launched,user_name, password,user,dbname, pw_db]
        update(args,credentials)
    else:
        user_name = config.user_name
        password = config.password
        user = config.dbuser
        pw_db = config.dbpw
        dbname = config.dbname
    return launched,user_name, password,user,pw_db,dbname

def run(n,p,a,b,c):
    print("----------------------------------------------------------------------")
    passw = input(f'Please provide the master password to start using {n}: ')
    print("----------------------------------------------------------------------")
    if passw == decrypt_pw(p):
        print('You\'re in')

    else:
        print('no luck')
        exit() 

    choice = menu()
    while choice != 'Q':
        if choice == '1':
            create(a,b,c)
        if choice == '2':
            find_accounts(a,b,c)
        if choice == '3':
            find(a,b,c)
            choice = menu()
        elif choice == '4':
            choice = delAccount(a, b, c)
        else:
            choice = menu()


#if  __name__ == "__main__":
launch()

run(user_name, password,user,pw_db,dbname)

