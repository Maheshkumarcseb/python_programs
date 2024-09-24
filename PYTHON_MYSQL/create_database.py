import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345')
cur=db1.cursor()
cur.execute('create database student')