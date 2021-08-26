# -*- coding:utf-8 -*-
import pyodbc
from classes import User_db

con_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=sql.athena.domainhizmetleri.com;'
        'DATABASE=mustaf11_Stok_Demo;'
        'UID=mustaf11_sencan;'
        'PWD=Mustiler463!'



)
con_str2 = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-QVEIDUC;'
        'DATABASE=zen;'
        'Trusted_Connection=yes;'




)
con = pyodbc.connect(con_str)






cursor = con.cursor()


def select_user():
    con = pyodbc.connect(con_str)
    cursor = con.cursor()
    query = "SELECT * FROM users "
    cursor.execute(query)
    rows = []
    for data in cursor:
        rows.append(User_db(data[0],data[1]))
    return rows
    print(rows)


def validate(username,password):
    quer1 = "SELECT User_password FROM Users where User_name = '%s' " % username
    cursor.execute(quer1)
    for data in cursor:
        print(data[0])
        print(password)
        if data[0].strip()==password.strip():
            return True
            
        else:
            return False


