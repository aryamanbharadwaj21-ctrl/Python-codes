import csv
f=open("18. sports performance details.csv","w")
writer=csv.writer(f)
fieldname=["Sports Competition Name","Score","Number of Prices Won"]
writer.writerow(fieldname)
n=int(input("Enter the number of prices won: "))
for i in range(n):
    n=[]
    c=input("Enter the name of competition: ")
    n.append(c)
    s=int(input("Enter the score: "))
    n.append(s)
    p=int(input("Enter the no. of prices won: "))
    n.append(p)
    writer.writerow(n)
    print("Sports detail record stored successfuly")
f.close()
    
