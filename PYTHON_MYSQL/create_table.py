import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()
s='create table details(roll_no int , name varchar(20),marks float)'
cur.execute(s)