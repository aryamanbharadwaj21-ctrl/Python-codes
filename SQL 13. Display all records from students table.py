import mysql.connector as ctr
con=ctr.connect(host='localhost',user='root',password='.',database='GARMS')
cursor=con.cursor()
cursor.execute('select * from students')
data=cursor.fetchall()
for i in data:
    print(i)
con.close()
