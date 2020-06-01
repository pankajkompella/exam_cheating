
import sqlite3 as lite
from tkinter import *

class packet:
    data= {}

    __instance = None
    __db_conn = None
    __window = None
    __frame = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if packet.__instance == None:
            packet.__instance = packet()
        return packet.__instance


    @staticmethod
    def set(key,value):
        p = packet.getInstance()
        p.data[key] = value

    @staticmethod
    def get(key):
        p = packet.getInstance()
        if key in p.data:
            return p.data[key]
        else:
            return None

    # connect to the database
    @staticmethod
    def dbconnect(db_name=None):
        """ Static access method. """
        if packet.__db_conn == None:
            try:
                packet.__db_conn = lite.connect(db_name)
            except lite.Error as e:
                print("Some error - " + e)
        return packet.__db_conn

    @staticmethod
    def window(name='My application'):
        """ Static access method. """
        if packet.__window == None:
            packet.__window = Tk()
            packet.__window.title(name)
        return packet.__window


    @staticmethod
    def loadFrame():
        """ Static access method. """
        if packet.__frame != None:
            packet.__frame.destroy()

        window = packet.window()
        packet.__frame = Frame(window,padx=10, pady=10)
        packet.__frame.grid()
        return packet.__frame

    # to insert, update or delete one record into table
    @staticmethod
    def execute(query):
        conn = packet.dbconnect()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()  # commit will save the data
        except lite.Error as e:
            print("Some error - " + e)

    # fetch all records from table
    @staticmethod
    def fetchall( query):
        conn = packet.dbconnect()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except lite.Error as e:
            print("Some error - " + e)
        return None

    # fetch one record from table
    @staticmethod
    def fetchone( query):
        conn = packet.dbconnect()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except lite.Error as e:
            print("Some error - " + e)
        return None

    # close the connection
    @staticmethod
    def dbclose():
        try:
            packet.__db_conn.close()
        except lite.Error as e:
            print("Some error - " + e)