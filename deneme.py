import pyodbc
from classes import User_db




con_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=sql.athena.domainhizmetleri.com;'
        'DATABASE=mustaf11_Stok_Demo;'
        'UID=mustaf11_sencan;'
        'PWD=Mustiler463!'



)
conn = pyodbc.connect(con_str)
username = "deneme"
cursor = conn.cursor()


cursor.execute("INSERT INTO de(ad,adet) VALUES(?,?)",[name,count])