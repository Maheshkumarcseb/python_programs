import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()

s='delete from details where roll_no =3'
# s='delete from details' ---> for deleting whole table
cur.execute(s)
db1.commit()