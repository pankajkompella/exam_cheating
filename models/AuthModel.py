from lib.db import *

class AuthModel:

    def __init__(self):
        self.conn = connect('app.db')

    def insert(self):
        query = 'INSERT INTO users (message) VALUES ("first")'
        insert(self.conn,query)

    def checkUser(self,username,password):
        query = 'SELECT * FROM users WHERE username ="'+username+'" and password="'+password+'"'
        result = fetchone(self.conn, query)
        return result

    def saveUser(self,name,phone,email,username,password):
        query = 'INSERT INTO users (name,phone,username,password,role) VALUES ("'+name+'",'+phone+',"'+username+'","'+password+'","student")'
        try:
            insert(self.conn, query)
            return 1
        except:
            return 0

if __name__ == '__main__':
    am = AuthModel()

