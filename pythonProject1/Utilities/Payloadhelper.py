from Utilities.Configuration import *


def getsingleentry(query):
    argatr={}
    row=getoneentryfromsql(query)
    argatr['CourseName']=row[0]
    argatr['PurchageDate']=row[1]
    argatr['Amount']=row[2]
    argatr['Location']=row[3]
    return argatr

def getoneentryfromsql(query):
    con=getmysqlconn()
    cursor=con.cursor()
    cursor.execute(query)
    row=cursor.fetchone()
    # print(row)
    return row
