import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()
r=int(input("enter your rollno:\n"))
n=input("enter your name:\n")
m=float(input("enter your marks"))
s='insert into details values(%s,%s,%s)'
t=(r,n,m)
cur.execute(s,t)
db1.commit()