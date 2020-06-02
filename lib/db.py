import sqlite3 as lite

# connect to the database
def connect(database_name):
    try:
        conn = lite.connect(database_name)
        return conn
    except lite.Error as e:
        print(e)

# To execute sql query
def execute(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print(e)

# insert one record into table
def insert(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit() # saves the data onto the disk
    except lite.Error as e:
        print(e)

# fetch all records from table
def fetchall(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print(e)

# fetch one record from table
def fetchone(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except lite.Error as e:
        print(e)
# update one record in the table
def update(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit() # saves the data onto the disk
    except lite.Error as e:
        print(e)

# delete one record from table
def delete(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit() # saves the data onto the disk
    except lite.Error as e:
        print(e)
# close the connection
def close(connection):
    try:
        connection.close()
    except lite.Error as e:
        print(e)
