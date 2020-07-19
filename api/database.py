# import sqlite3
# from sqlite3 import Error
# from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import errorcode
from classes import Ratio
import json


Database = "mutants"
Table = "dna"


def getConn():
    try:
        # conn = mysql.connector.connect(host="localhost", user="root",
        #                             password="e3231441221", database=Database)
        conn = mysql.connector.connect(unix_socket='xmen-283720:southamerica-east1:database1',
                                    user="root", password="e3231441221", database=Database)
        print(conn)
        
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.close()

def postDna(dna, isMutant):
    conn = getConn()
    try:
        cursor = conn.cursor()
        strDna = str(json.dumps(dna))

        query = "SELECT * FROM dna WHERE dna = %s"
        cursor.execute(query, (strDna,))
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("INSERT INTO dna(dna, isMutant) \
                            values('{0}', '{1}')".format(strDna, isMutant))
            print('New dna saved.')
        else:
            print('Dna already saved.')
        
        conn.commit()
        cursor.close()
    except:
        print('Error')
    conn.close()

def getStats():
    conn = getConn()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT isMutant, COUNT(isMutant) \
                                 AS ammount FROM dna GROUP BY isMutant") 
        mutantsCount = 0
        humansCount = 0
        ratioCalc = 0
        for (isMutant, ammount) in cursor:
            if isMutant == 0:
                humansCount = ammount
            else:
                mutantsCount = ammount

        if humansCount > 0:
            ratioCalc = float("{:.2f}".format((mutantsCount / humansCount)))

        cursor.close()
        ratio = Ratio(mutantsCount, humansCount, ratioCalc)
        return json.dumps(ratio.__dict__)
    except:
        print('Error')
    conn.close()

