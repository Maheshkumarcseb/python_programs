import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()
s='update details set marks = marks +2 where roll_no=4'

cur.execute(s)
db1.commit()