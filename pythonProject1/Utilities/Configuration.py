import configparser
import mysql.connector
from mysql.connector import Error


def getconfing():
    config=configparser.ConfigParser()
    config.read('Utilities/Properties.ini')
    return config
def geturl():
    config=getconfing()
    return config['API']['url']

mysqlattribures={
    'user':getconfing()['SQL']['user'],
    'password':getconfing()['SQL']['password'],
    'host':getconfing()['SQL']['host'],
    'database':getconfing()['SQL']['database']
}

def getmysqlconn():
    try:
        con=mysql.connector.connect(**mysqlattribures)
        if con.is_connected()==True:
            print("Successfully connected!")
            return con
    except Error as e:
        print(e)

def getsqlconfing():
    sqlconfig=configparser.ConfigParser()
    sqlconfig.read('Utilities/Queries.ini')
    return sqlconfig
def getqueryparser():
    return getsqlconfing()['Queries']


def getsqlcursor():
    conn=getmysqlconn()
    curs=conn.cursor()
    return curs

def fetchoneentry(query):
    curs=getsqlcursor()
    curs.execute(query)
    row=curs.fetchone()
    return row