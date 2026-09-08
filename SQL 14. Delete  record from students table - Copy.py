import mysql.connector as ctr
con=ctr.connect(host='localhost',user='root',password='.',database='GARMS')
cursor=con.cursor()
choice='y'
choice=input("Do you want to delete records?: ")
while choice!='y' and choice!='N' and choice!='Y' and choice!='n':
    if choice!='y' or choice!='N' or choice!='Y' or choice!='n':
        choice=input("Invalid input! Do you want to delete records?: ")
        if choice=='y' or choice=='n' or choice=='N' or choice=='Y5':
            break
while choice=='y' or choice=='Y':
    name=input("Enter the name of student whose record you want to delete: ")
    cursor.execute("DELETE FROM students WHERE Name = %s", (name,))
    con.commit()
    print("Record of",name,"deleted successfully")
    choice=input("Do you want to delete records? ")
cursor.execute("select * from students")
data=cursor.fetchall()
for i in data:
    print (i)
con.close()
