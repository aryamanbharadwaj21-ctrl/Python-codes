import pickle
stu={}
found=False
f=open("Stu.dat",mode="rb+")
try:
    while True:
        s=f.tell()
        stu=pickle.load(f)
        if stu["Marks"]>81:
            stu["Marks"]+=2
            f.seek(s)
            pickle.dump(stu,f)
            found=True
except EOFError:
    if found==False:
        print("No records found.")
    else:
        print("Bonus marks successfully added")
        f.close()
f=open("Stu.dat","rb+")
try:
    while True:
        stu=pickle.load(f)
        print(stu)
except EOFError:
        f.close()
