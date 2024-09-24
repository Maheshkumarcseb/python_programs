import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()
## insert the value into tuples through 
s='insert into details values(%s,%s,%s)'

t=[(3,"Arya",56),(4,"sudin",45)]

cur.executemany(s,t)
db1.commit()