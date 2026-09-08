import pickle
found=False
f=open("Student.dat","rb")
rollno=[12,14]
try:
    while True:
        stu=pickle.load(f)
        if stu["Roll Number"] in rollno:
            print(stu)
            found=True
except EOFError:
    if found==False:
        print("No records found.")
        f.close()
    else:
        f.close()
