def countlines():
    f=open("14 Display Number of Lines.txt")
    a=f.readlines()
    no=len(a)
    print("The number of lines are: ",no)
    f.close()
countlines()
