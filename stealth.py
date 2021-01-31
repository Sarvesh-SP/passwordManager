import psycopg2
user = "postgres"
pw = "sarve"
db_name = "passwordmanager"



def store_p(password, user_email, username, url, website):
    try:
        connection = conne("postgres", "sarve","passwordmanager")
        cursor = connection.cursor()
        website_insert = """ INSERT INTO website (web) VALUES (%s)"""
        website_to_insert = (website, )
        cursor.execute(website_insert, website_to_insert)
        connection.commit()


        email_insert = """ INSERT INTO email (mail) VALUES (%s)"""
        email_to_insert = (user_email, )
        cursor.execute(email_insert, email_to_insert)
        connection.commit()

        user_insert = """ INSERT INTO username (username) VALUES (%s)"""
        user_to_insert = (username, )
        cursor.execute(user_insert, user_to_insert)
        connection.commit()

        password_insert = """ INSERT INTO password (password) VALUES (%s)"""
        password_to_insert = (password, )
        cursor.execute(password_insert, password_to_insert)  
        connection.commit()

        url_insert = """ INSERT INTO url (url) VALUES (%s)"""
        url_to_insert = (url, )
        cursor.execute(url_insert, url_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def conne(user,pw,db_name):
    try:
        connection = psycopg2.connect(user="postgres", password="sarve", host='localhost', database="passwordmanager")
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_p(website):
    try:
        connection = psycopg2.connect(user="postgres", password="sarve", host='localhost', database="passwordmanager")
        cursor = connection.cursor()
        postgres_select_query = f"SELECT p.password, w.web, e.mail, l.url, u.username from username u, password p, website w, email e, url l where w.web = '{website}' and p.sno = w.sno and e.sno = w.sno and l.sno = w.sno and u.sno = w.sno"
        cursor.execute(postgres_select_query, website)
        connection.commit()
        result = cursor.fetchall()
        data = ('Password: ', 'Website: ', 'Email: ', 'url: ', 'Username: ')
        for row in result:
            for i in range(0, len(row)):
                print('-'*50)
                print(data[i] + row[i])
        print('')
        print('-'*50)
    
    except (Exception, psycopg2.Error) as error:
        print(error)
def find_u(user_email):
    data = ('Website: ', 'Email: ', 'url: ', 'Username: ')
    try:
        connection = psycopg2.connect(user="postgres", password="sarve", host='localhost', database="passwordmanager")
        cursor = connection.cursor()

        try:
            postgres_select_query = f"select w.web, e.mail, l.url, u.username from url l, website w, username u, email e where e.mail = '{user_email}' and e.sno = u.sno and e.sno = w.sno and e.sno = l.sno"
            cursor.execute(postgres_select_query, user_email)
        except (Exception, psycopg2.Error) as error:
            print(f"Email does'nt exist.{error}")
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)):
                print('-'*50)
                print(data[i] + row[i])
            print('*'*50)
        print('')
        print('-'*50)
    except (Exception, psycopg2.Error) as error:
        print(error)

def delUser(username):
    try:
        connection = psycopg2.connect(user="postgres", password="sarve", host='localhost', database="passwordmanager")
        cursor = connection.cursor()
        try:
            delQuery = f"delete from website w where w.sno = (select u.sno from username u where u.username = '{username}')"
            cursor.execute(delQuery, username)
        except (Exception, psycopg2.Error) as error:
            print(error)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
