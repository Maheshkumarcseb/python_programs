import mysql.connector

db1=mysql.connector.connect(host='localhost',user='root',password='12345',database ='student')
cur=db1.cursor()

s='select * from details'
cur.execute(s)
r=cur.fetchall()
# r=cur.fetchone()
print(r)

for i in r:
    # print(i)
    for j in i:
        print(j,end=" ")
    print()