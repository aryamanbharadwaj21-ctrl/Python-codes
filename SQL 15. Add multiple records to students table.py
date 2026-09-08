import mysql.connector as ctr
con=ctr.connect(host='localhost',user='root',password='.',database='GARMS')
cursor=con.cursor()
choice='y'
choice=input("Do you want to add records?: ")
while True:
    if choice!='y' and choice!='N' and choice!='Y' and choice!='n':
        choice=input("Invalid input! Do you want to add records?: ")
    else:
        break
while choice=='y' or choice=='Y':
    rno=int(input("Enter the roll number of student: "))
    name=input("Enter the name of student : ")
    age=int(input("Enter the age of student: "))
    print("Enter the marks out of 100 in the following subjects: ")
    eng=int(input("English: "))
    phy=int(input("Physics: "))
    chem=int(input("Chemistry: "))
    maths=int(input("Mathematics: "))
    cs=int(input("Computer Science: "))
    cursor.execute("insert into students values ({},'{}',{},{},{},{},{},{})".format(rno,name,eng,phy,chem,maths,cs,age))
    con.commit()
    print("Record of",name,"added successfully")
    choice=input("Do you want to add more records? ")
cursor.execute("select * from students")
data=cursor.fetchall()
for i in data:
    print (i)
con.close()
