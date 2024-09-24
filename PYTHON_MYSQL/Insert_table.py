import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()
s='insert into details values(1,"kartik",65)'
cur.execute(s)
t='insert into details values(2,"abhas",43)'
cur.execute(t)

db1.commit()