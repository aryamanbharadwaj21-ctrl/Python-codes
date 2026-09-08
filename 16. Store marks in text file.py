def storemarks():
    f=open("Marks.txt","w")
    n=int(input("Enter the number of students: " ))
    for i in range(n):
        r=input("Enter the roll number: ")
        rollno="Roll No.: "+r
        n=input("Enter the name: ")
        name="Name: "+ n
        m=input("Enter the marks: ")
        marks="Marks: "+m
        details=rollno+",   "+name+",   "+marks+"\n"
        f.write(details)
    print("Records added successfully.")
    f.close()
storemarks()
        
