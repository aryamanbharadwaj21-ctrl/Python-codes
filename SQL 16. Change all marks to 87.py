import mysql.connector as ctr
con=ctr.connect(host='localhost',user='root',password='.',database='GARMS')
cursor=con.cursor()
cursor.execute('update students set Eng=87,Phy=87,Chem=87,Maths=87,Comp_Sci=87 where Rno=5')
print("Marks updated successfully.")
con.commit()
cursor.execute('select * from students where Rno=5')
data=cursor.fetchall()
for i in data:
    print(i)
con.close()
