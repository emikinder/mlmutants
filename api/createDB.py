import mysql.connector
from mysql.connector import errorcode

Database = "mutants"
Table = "dna"

def run():
    createDatabase()
    createTable()

def createDatabase():
    conn = mysql.connector.connect(host="localhost", user="root",
                                password="root")
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mutants")
    except:
        print('Error createDatabase.')

def createTable():
    conn = mysql.connector.connect(host="localhost", user="root",
                                password="root", database="mutants")
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE `dna` (`id` int NOT NULL AUTO_INCREMENT,`dna` longtext NOT NULL,`isMutant` tinyint(1) NOT NULL DEFAULT '0',PRIMARY KEY (`id`),UNIQUE KEY `id_UNIQUE` (`id`))")
    except:
        print('Error createTable.')


if __name__ == '__main__':
    run()