def isempty(arr):
    if arr==[]:
        top=None
        return True
    else:
        return False
def push(arr,item):
    arr.append(item)
    top=len(arr)-1
def Pop(arr):
    if isempty(arr):
        top=None
        return("Underflow")
    else:
        arr.pop()
        top=len(arr)-1
def display(arr):
    if isempty(arr):
        return("Stack empty.")
    else:
        top=len(arr)-1
        for i in arr[::-1]:
            print(i)
l=[]    
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    ch=input("Enter choice: ")
    if ch=="1":
        no=int(input("Enter membership number: "))
        name=input("Enter member name: ")
        age=int(input("Enter member age: "))
        member=[no,name,age]
        push(l,member)    
        print("Member added successfully.")
    elif ch=="2":
        if l==[]:
            print("Nothing to delete.")
        else:
            Pop(l)
            print("Member deleted successfully.")
    elif ch=="3":
        print(display(l))
    elif ch=="4":
        break
    else:
        print("Invalid input. ")
