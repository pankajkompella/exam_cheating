from lib.packet import packet as p

class AuthModel:

    def __init__(self):
        p.dbconnect('app.db')

    def insert(self):
        query = 'INSERT INTO users (message) VALUES ("first")'
        p.insert(query)

    def checkUser(self,username,password):
        query = 'SELECT * FROM users WHERE username ="'+username+'" and password="'+password+'"'
        return p.fetchone(query)
