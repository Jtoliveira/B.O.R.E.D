import uuid
import hashlib
import sqlite3
import random

#hash_password() and check_password() from https://www.pythoncentral.io/hashing-strings-with-python/

class Login:

    def __init__(self, fileName):
        self.fileName = fileName

    def databaseSetup(self):
        #create database 'users' in the current directory if it doesn't exist already
        conn = sqlite3.connect('users.db')
        print ("Opened database successfully")
        #creating the users table
        try:
            conn.execute("CREATE TABLE USERS (ID INT PRIMARY KEY NOT NULL, USERNAME TEXT NOT NULL,PASSWORD TEXT NOT NULL, SALT TEXT NOT NULL);")
        except:
            print("Table already exists!")
        conn.close()
    
    def createUser(self,name,password):

        hashed_password = self.hash_password(password)

        password, salt = hashed_password.split(':')

        conn = sqlite3.connect('users.db')

        conn.execute("INSERT INTO USERS (ID,USERNAME,PASSWORD, SALT) VALUES (?,?,?,?)", (str(random.randint(1,10000000)),name,password,salt))

        conn.commit()

        conn.close()
            
    def checkIfUserAlreadyExists(self,name):
        result = False

        conn = sqlite3.connect('users.db')

        cursor = conn.execute("SELECT ID,USERNAME,PASSWORD,SALT FROM USERS WHERE USERNAME = ?", (name,))

        if len(cursor.fetchall()) == 1:
            result = True

        conn.close()
    
        return result

    def checkUserLogin(self, name, password):
        
        result = False

        conn = sqlite3.connect('users.db')

        cursor = conn.execute("SELECT ID,USERNAME,PASSWORD,SALT FROM USERS WHERE USERNAME = ?", (name,))

        for row in cursor:
            if row[1] == name and self.check_password(row[2] + ":" + row[3], password):
                result = True
                
        conn.close()

        return result
            
    def hash_password(self,password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt #it creates a hashed password in the format password:salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


