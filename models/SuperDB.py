import sqlite3 as lite

class Super:

    # connect to the database
    def connect(self,database_name):
        try:
            self.conn = lite.connect(database_name)
        except lite.Error as e:
            print("Some error - " + e)

    # insert one record into table
    def insert(self,query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit() # commit will save the data
        except lite.Error as e:
            print("Some error - " + e)

    # fetch all records from table
    def fetchall(self,query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except lite.Error as e:
            print("Some error - " + e)

    # fetch one record from table
    def fetchone(self,query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except lite.Error as e:
            print("Some error - " + e)

    # update one record in the table
    def update(self,query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            conn.commit()
        except lite.Error as e:
            print("Some error - " + e)

    # delete one record from table
    def delete(self,query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            conn.commit()
        except lite.Error as e:
            print("Some error - " + e)

    # close the connection
    def close(self):
        self.conn.close()